from django.urls import path
from users import views

urlpatterns = [
    path('registry/', views.UserRegistryView.as_view(), name='registry'),
    path('email-verification/', views.VerifyEmailView.as_view(), name='email-verification'),
    path('usernames/', views.LiveSearchUsernameAvailabilityView.as_view(), name='usernames'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('test/', views.TestView.as_view())
]

