from django.urls import path
from .views import predict_category, login_view, register_view

urlpatterns = [
    path('predict/', predict_category, name='predict_category'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),  # NEW!

]