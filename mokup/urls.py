from django.urls import path
from . import views

# Define URL patterns for the app
urlpatterns = [

 path('register/', views.signup, name='signup'),
 path('home/',views.homepage,name = 'home'),
 path('login/', views.user_login, name='login'),
]