from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bInternational = models.BooleanField(max_length=20)
    gender = models.CharField(max_length=1)
    email = models.CharField(max_length=30)
    fExpectedHours = models.FloatField(max_length=4)
    sSemester = models.CharField(max_length=10)
    iYear = models.IntegerField()
    sPhone = models.CharField(max_length=12)
    sBYUID = models.CharField(max_length=12)
    sPositionType = models.CharField(max_length=12)
    sClassCode = models.CharField(max_length=10)
    iEmployeeRecord = models.IntegerField()
    sSupervisior = models.CharField(max_length=15)
    dDate = models.DateField(max_length=10)
    fPayRate = models.FloatField(max_length=6)
    dLastPayIncrease = models.DateField(max_length=10)
    fIncreaseAmount = models.FloatField(max_length=6)
    dIncreaseInput = models.DateField(max_length=6)
    sYearInProgram = models.CharField(max_length=10)
    bPayGradTuition = models.BooleanField(max_length=1)
    bNameChangeCompleted = models.BooleanField(max_length=1)
    sNotes = models.CharField(max_length=255)
    bTerminated = models.BooleanField(max_length=1)
    dTerminationDate = models.DateField(max_length=6)
    bQualtricsSurveySent = models.BooleanField(max_length=1)
    bSubmittedEForm = models.BooleanField(max_length=1)
    dEFormSubmitted = models.DateField(max_length=6)
    bAuthroizedToWork = models.BooleanField(max_length=1)
    dAuthorizationWorkEmailSent = models.DateField(max_length=6)
    sBYUName = models.CharField(max_length=30)

    class Meta:
        db_table = "Student"

    def __str__(self):
        return (self.material_name)