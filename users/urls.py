from django.urls import path
from users import views

urlpatterns = [
    path('registry/', views.UserRegistryView.as_view())
]
