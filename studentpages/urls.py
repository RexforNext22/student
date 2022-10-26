# Import the django.url and views function
from django.urls import path
from .views import indexPageView
from .views import libraryPageView
from .views import newPageView
from .views import aboutPageView




# Create the different path for index and about 
urlpatterns = [
    path("", indexPageView, name="index"),
    path("/library", libraryPageView, name="library"),
    path("/new", newPageView, name="new"),
    path("/about", aboutPageView, name="about"),                 
        ]        
