from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to the Budget Tracker API!</h1><p>Use <code>/api/predict/</code> to POST transactions.</p>")

