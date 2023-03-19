from django.db import models
# Create your models here.
class Student(models.Model):

    genderChoices = (
        ('one', 'Male'),
        ('two', 'Female')
    )
    schoolLevelChoices = (
        ('one', '8 Complete'),
        ('two', '10 Complete'),
        ('three', '12 Complete'),
        ('four', 'Diploma'),
        ('five', 'Degree'),
        ('six', 'Masters'),
        ('seven', 'Vocational school'),
    )
    convinintTiming = (
        ('one', '9AM - 11AM'),
        ('two', '12PM - 2PM'),
        ('three', '3PM - 5PM'),
        ('four', '6PM - 8PM')
    )

    name = models.CharField( max_length=100)
    age = models.IntegerField(blank=True)
    gender = models.CharField( max_length=100, choices=genderChoices,verbose_name="Gender")
    phoneNumber = models.CharField( max_length=13)
    email = models.EmailField( max_length=100, blank=True)
    SchoolLevel = models.CharField( max_length=100, choices= schoolLevelChoices, blank=True,verbose_name="School Level")
    priorProgrammingBackground = models.BooleanField(default=False, blank= True,verbose_name="Do you have previous programming experiance?")
    currentOccupation = models.CharField( max_length=100, blank=True)
    convinientTime = models.CharField( max_length=100, choices= convinintTiming, verbose_name="What time is convinient for you?")
    ReasonForAttendance = models.TextField(blank=True)
    howDidYouHearAboutUs = models.CharField( max_length=100,blank=True)
    isSelected = models.BooleanField(default=False, blank=True)

    def __str__(self):
        #return '%s %s'%(self.name, self.isSelected)
        return f'{self.name} {self.isSelected}'
    