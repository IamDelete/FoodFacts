from django.urls import path
from . import views

# Define URL patterns for the app
urlpatterns = [

 path('register/', views.signup, name='signup'),
 path('home/',views.homepage,name = 'home'),
 path('login/', views.user_login, name='login'),
    path('addfood/', views.add_food, name='add_food'),
    path('add/success/', views.food_add_success, name='food_add_success'),
    path('foodcatalog/', views.display_food, name='foodcatalog'),
]