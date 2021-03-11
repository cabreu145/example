from django.urls import path
from . import views
urlpatterns = [
    #paths index
    path('', views.home, name='home'),
    
    
]