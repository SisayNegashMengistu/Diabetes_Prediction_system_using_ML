
from django.shortcuts import render
from django.http import HttpResponseBadRequest
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
def home(request):
    return render(request,'home.html')
def predict(request):
    return render(request,'predict.html')
def result(request):
    data = pd.read_csv(r"C:\Users\user\machine learning project 2024\diabetes.csv")
    X = data.drop("Outcome", axis=1)
    Y = data["Outcome"]
    X_train, X_test, Y_train, y_test = train_test_split(X, Y, test_size=0.2)

    model = LogisticRegression()
    model.fit(X_train, Y_train)
    #user input
    # Get the value or an empty string if it's not provided
    val1 = request.GET.get('n1', '')
    val2 = request.GET.get('n2', '')
    val3 = request.GET.get('n3', '')
    val4 = request.GET.get('n4', '')
    val5 = request.GET.get('n5', '')
    val6 = request.GET.get('n6', '')
    val7 = request.GET.get('n7', '')
    val8 = request.GET.get('n8', '')
    # Check if any of the input values are empty strings
    if '' in [val1, val2, val3, val4, val5, val6, val7, val8]:
        # If any of the input fields are empty, return an error message
        error_message = "Please fill in all the input fields."
        return HttpResponseBadRequest(error_message)
    else:
        # Convert the input values to floats and proceed with prediction
        try:
            val1_float = float(val1)
            val2_float = float(val2)
            val3_float = float(val3)
            val4_float = float(val4)
            val5_float = float(val5)
            val6_float = float(val6)
            val7_float = float(val7)
            val8_float = float(val8)

            # Proceed with prediction
            pred = model.predict(
                [[val1_float, val2_float, val3_float, val4_float, val5_float, val6_float, val7_float, val8_float]])

            result1 = ""
            if pred == [1]:
                result1 = "Positive"
            else:
                result1 = "Negative"

            return render(request, 'predict.html', {"result2": result1})

        except ValueError:
            # Handle the case where any of the input values couldn't be converted to floats
            # You might want to return an error message or redirect the user to a form page.
            error_message = "Invalid input. Please provide valid numeric values."
            # Render the form page along with the error message (if any)
            return render(request, 'predict.html', {"error_message": error_message})