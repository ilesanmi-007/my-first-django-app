
from myfirstApp import views
from django.urls import path

#import myfirstApp.views
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')


urlpatterns = [
    path('home/', views.home , name = 'home'),
    path('index/', views.index, name = 'index')

]