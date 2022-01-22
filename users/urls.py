from django.urls import path
from users import views

urlpatterns = [
    path('registry/', views.UserRegistryView.as_view()),
    path('email-verification/', views.VerifyEmailView.as_view(), name='email-verification'),
]
