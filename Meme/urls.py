from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name= 'home'),
    path('memeTool', views.memeTool, name= 'memeTool'),
    path('uploadMeme', views.uploadMeme, name= 'uploadMeme'),
    path('viewMeme', views.viewMeme, name= 'viewMeme'),
    
]
