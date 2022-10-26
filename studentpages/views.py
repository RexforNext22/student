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
        oStudent.gender = request.POST.get('gender')
        oStudent.email = request.POST.get('email')
        oStudent.fExpectedHours = request.POST.get('fExpectedHours')
        oStudent.sSemester = request.POST.get('sSemester')
        oStudent.iYear = request.POST.get('iYear')
        oStudent.sPhone = request.POST.get('sPhone')
        oStudent.sBYUID = request.POST.get('sBYUID')
        oStudent.sPositionType = request.POST.get('sPositionType')
        oStudent.sClassCode = request.POST.get('sClassCode')
        oStudent.iEmployeeRecord = request.POST.get('iEmployeeRecord')
        oStudent.sSupervisior = request.POST.get('sSupervisior')
        oStudent.dDate = request.POST.get('dDate')
        oStudent.fPayRate = request.POST.get('fPayRate')
        oStudent.dLastPayIncrease = request.POST.get('dLastPayIncrease')
        oStudent.fIncreaseAmount = request.POST.get('fIncreaseAmount')
        oStudent.dIncreaseInput = request.POST.get('dIncreaseInput')
        oStudent.sYearInProgram = request.POST.get('sYearInProgram')
        oStudent.bPayGradTuition = request.POST.get('bPayGradTuition')
        oStudent.bNameChangeCompleted = request.POST.get('bNameChangeCompleted')
        oStudent.sNotes = request.POST.get('sNotes')
        oStudent.bTerminated = request.POST.get('bTerminated')
        oStudent.dTerminationDate = request.POST.get('dTerminationDate')
        oStudent.bQualtricsSurveySent = request.POST.get('bQualtricsSurveySent')
        oStudent.bSubmittedEForm = request.POST.get('bSubmittedEForm')
        oStudent.dEFormSubmitted = request.POST.get('dEFormSubmitted')
        oStudent.bAuthroizedToWork = request.POST.get('bAuthroizedToWork')
        oStudent.dAuthorizationWorkEmailSent = request.POST.get('dAuthorizationWorkEmailSent')
        oStudent.sBYUName = request.POST.get('sBYUName')



        oStudent.save()

    return render(request, 'studentpages/index.html')

def showSingleStudent(request, id):

    data = Student.objects.get(id=id)
    context = {
        "Student": data,
    }

    return render(request, 'studentpages/showSingleStudent.html', context)