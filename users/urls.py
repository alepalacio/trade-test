from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from users import views

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair',),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh',),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify',),
    path('registry/', views.UserRegistryView.as_view(), name='registry'),
    path('email-verification/', views.VerifyEmailView.as_view(), name='email-verification'),
    path('usernames/', views.LiveSearchUsernameAvailabilityView.as_view(), name='usernames'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout',),
    path('test/', views.TestView.as_view())
]

