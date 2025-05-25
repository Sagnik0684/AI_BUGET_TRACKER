from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import joblib
import os
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User



# Load model once when server starts
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, 'model.pkl')

model = joblib.load(model_path)

@csrf_exempt
def predict_category(request):
    if request.method == "POST":
        data = json.loads(request.body)
        description = data.get("description", "")
        if not description:
            return JsonResponse({"error": "No description provided."}, status=400)
        
        prediction = model.predict([description])[0]
        return JsonResponse({"category": prediction})

    return JsonResponse({"error": "Invalid method"}, status=405)



@csrf_exempt
def login_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # sets session
            return JsonResponse({"message": "Login successful"}, status=200)
        else:
            return JsonResponse({"error": "Invalid credentials"}, status=401)
    return JsonResponse({"error": "Invalid method"}, status=405)


@csrf_exempt
def register_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")

        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "Username taken"}, status=400)

        user = User.objects.create_user(username=username, password=password)
        user.save()
        return JsonResponse({"message": "User registered successfully"}, status=201)

    return JsonResponse({"error": "Invalid method"}, status=405)