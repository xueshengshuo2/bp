from django.urls import path
from . import views
app_name = 'bc'
urlpatterns = [
    path('', views.bc, name='bc'),
    
]