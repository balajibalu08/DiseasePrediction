# Disease Identification Chatbot

This is a simple chatbot application for disease identification based on symptoms. The chatbot uses a machine learning model to classify diseases and provide recommendations such as food and rest days.

## Project Structure

- `datasets/`: Contains the dataset CSV file.
- `models/`: Contains the trained model and vectorizer files.
- `static/`: Contains static files such as CSS.
- `templates/`: Contains HTML template files.
- `app.py`: Flask application script.
- `disease_classifier.py`: Script to train the disease classification model.
- `requirements.txt`: List of required Python packages.
- `README.md`: Project documentation.

## Setup

1. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

2. Train the disease classification model:
    ```bash
    python disease_classifier.py
    ```

3. Run the Flask application:
    ```bash
    python app.py
    ```

4. Open your web browser and go to `http://127.0.0.1:5000`.

## Usage

Enter symptoms in the input field and submit the form to get disease identification and recommendations.

