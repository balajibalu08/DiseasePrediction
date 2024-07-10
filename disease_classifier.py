import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

# Load dataset
data = pd.read_csv('datasets/disease_data.csv')

# Feature extraction
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data['symptoms'])

# Labels
y = data['disease']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Save model and vectorizer
joblib.dump(model, 'models/disease_model.pkl')
joblib.dump(vectorizer, 'models/vectorizer.pkl')

print("Model trained and saved successfully.")
