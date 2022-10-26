from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

def indexPageView(request) :
    return render(request, 'studentpages/index.html')

def libraryPageView(request) :

    data = Student.objects.all()
    context = {
        "Student": data,
    }

    return render(request, 'studentpages/library.html', context)

def newPageView(request) :
    return render(request, 'studentpages/new.html')

def aboutPageView(request) :
    return render(request, 'studentpages/about.html')

def savePageView(request):
    if request.method == 'POST':
        oStudent = Student()

        oStudent.first_name = request.POST.get('first_name')
        oStudent.last_name = request.POST.get('last_name')
        oStudent.bInternational = request.POST.get('bInternational')


        # print(oArticleOfClothing)
        oStudent.save()

    return render(request, 'studentpages/index.html')