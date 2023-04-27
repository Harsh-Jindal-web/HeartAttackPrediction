from django.shortcuts import render
from django.http import HttpResponse
import pickle
import os


# Load the pre-trained SVM model from the pickle file
with open('model.pkl', 'rb') as file:
    svm_model = pickle.load(file)

# View for handling form submission
def predict(request):
    if request.method == 'POST':
        # Get user input from form data
        age = float(request.POST['age'])
        sex = float(request.POST['sex'])
        cp = float(request.POST['cp'])
        trestbps = float(request.POST['trestbps'])
        chol = float(request.POST['chol'])
        # fbs = float(request.POST['fbs'])
        restecg = float(request.POST['restecg'])
        thalach = float(request.POST['thalach'])
        exang = float(request.POST['exang'])
        # oldpeak = float(request.POST['oldpeak'])
        slope = float(request.POST['slope'])
        ca = float(request.POST['ca'])
        thal = float(request.POST['thal'])

        # Create a dictionary to hold the user input
        user_input = {
            'age': age,
            'sex': sex,
            'cp': cp,
            'trestbps': trestbps,
            'chol': chol,
            # 'fbs': fbs,
            'restecg': restecg,
            'thalach': thalach,
            'exang': exang,
            # 'oldpeak': oldpeak,
            'slope': slope,
            'ca': ca,
            'thal': thal
        }

        # Make prediction
        # prediction = predict(user_input, svm_model)
        prediction = svm_model.predict([list(user_input.values())])

        # Display the prediction
        if prediction[0] == 0:
            result = "Based on the provided input, The chances of Heart attack are Low."
        else:
            result = "Based on the provided input, The chances of Heart attack are High."

        return render(request, 'main/result.html', {'result': result})

    return render(request, 'main/index.html')


