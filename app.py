from flask import Flask, request, render_template
import joblib
import pandas as pd

# Load model and vectorizer
model = joblib.load('models/disease_model.pkl')
vectorizer = joblib.load('models/vectorizer.pkl')

# Load dataset
data = pd.read_csv('datasets/disease_data.csv')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        symptoms = request.form['symptoms']
        if not symptoms:
            raise ValueError("No symptoms provided")
        
        symptoms_vect = vectorizer.transform([symptoms])
        disease = model.predict(symptoms_vect)[0]
        
        # Get disease info
        disease_info = data[data['disease'] == disease].iloc[0]
        food = disease_info['food'].split(';')
        rest_days = disease_info['rest_days']
        medications = disease_info['medications'].split(';') if pd.notna(disease_info['medications']) else []
        nearby_hospitals = disease_info['nearby_hospitals'].split(';') if pd.notna(disease_info['nearby_hospitals']) else []
        
        return render_template('index.html', disease=disease, food=food, rest_days=rest_days, medications=medications, nearby_hospitals=nearby_hospitals)
    except Exception as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=False)
