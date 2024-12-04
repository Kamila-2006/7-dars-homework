from django.urls import path
from . import views


app_name = 'cars'
urlpatterns = [
    path('list/', views.cars_list, name="list"),
    path('create/', views.car_create, name="create")
]