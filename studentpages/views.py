from django.shortcuts import render
from django.http import HttpResponse

def indexPageView(request) :
    return render(request, 'studentpages/index.html')

def libraryPageView(request) :
    return render(request, 'studentpages/library.html')

def newPageView(request) :
    return render(request, 'studentpages/new.html')

def aboutPageView(request) :
    return render(request, 'studentpages/about.html')