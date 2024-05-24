Diabetes Prediction System
Overview

This project implements a diabetes prediction system using machine learning techniques. The system takes various health-related features as input and predicts whether a person is likely to have diabetes or not.
Table of Contents

    Requirements
    Installation
    Usage
    Dataset
    Model Training
    Evaluation
    Contributing
    License

Requirements

    Python 3.12.3
    Django
    scikit-learn 1.5.0
    pandas

Installation

    Clone the repository:

    bash

git clone https://github.com/yourusername/Diabetes_Prediction_system_using_ML.git

Navigate to the project directory:

bash

cd diabetes-prediction

Install dependencies:

    pip install -r requirements.txt

Usage

    Run the Django server:

    python manage.py runserver

    Access the application in your web browser at http://127.0.0.1:5500.
    Use the provided interface to input health-related features and get predictions for diabetes.

Dataset

The dataset used for training the prediction model is diabetes.csv, which contains various health-related features and the corresponding diabetes outcome (0 for non-diabetic, 1 for diabetic).
Model Training

The prediction model is trained using logistic regression on the provided dataset. The training process involves splitting the dataset into training and testing sets, fitting the model on the training data, and evaluating its performance.
Evaluation

The performance of the prediction model can be evaluated using various metrics such as accuracy, precision, recall, and F1-score. These metrics provide insights into how well the model predicts the presence or absence of diabetes.
Contributing

Contributions to this project are welcome! If you find any issues or have suggestions for improvements, please open an issue or create a pull request.
License

This project is licensed under the BDU License.
