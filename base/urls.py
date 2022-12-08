from django.urls import path
from . import views

urlpatterns = [
    path('', views.getInput, name='get_input_url'),
    path('/data', views.data, name='data'),
    
    #CRUD Urls
    
    
]
