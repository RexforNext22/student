# Import the django.url and views function
from django.urls import path
from .views import UpdatePageView, indexPageView
from .views import libraryPageView
from .views import newPageView
from .views import aboutPageView
from .views import savePageView
from .views import showSingleStudent
from .views import EditPageView
from .views import UpdatePageView
from .views import DeletePageView





# Create the different path for index and about 
urlpatterns = [
    path("", indexPageView, name="index"),
    path("library/", libraryPageView, name="library"),
    path("new/", newPageView, name="new"),
    path("about/", aboutPageView, name="about"),
    path("save/", savePageView, name="save"),
    path("showSingleStudent/<int:id>/", showSingleStudent, name="showSingleStudent"),
    path("edit/<int:id>", EditPageView, name="edit"),
    path("update/<int:id>", UpdatePageView, name="update"),     
    path("delete/<int:id>", DeletePageView, name="delete"),            
        ]        
