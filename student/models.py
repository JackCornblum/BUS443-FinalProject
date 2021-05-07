from django.db import models

# Create your models here.

class Studentinfo(models.Model):
    studentid = models.IntegerField()
    fname = models.CharField(max_length=500)
    lname = models.CharField(max_length=500)
    major = models.CharField(max_length=500)
    year = models.CharField(max_length=500)
    gpa = models.FloatField()

class Courseinfo(models.Model):
    courseid = models.IntegerField()
    coursetitle = models.CharField(max_length=500)
    coursename = models.CharField(max_length=500)
    sectionid = models.IntegerField()
    coursedepartment = models.CharField(max_length=500)
    instructorname = models.CharField(max_length=500)

class Dashboardinfo(models.Model):
    avgGpa = models.FloatField()
    totalIT = models.FloatField(default=0)
    totalphysics = models.FloatField(default=0)
    totalmarketing = models.FloatField(default=0)
    totalchem = models.FloatField(default=0)
    totalstats = models.FloatField(default=0)

class Enrollmentinfo(models.Model):
    studentname = models.CharField(max_length=500)

class Enrollment(models.Model):
    student = models.CharField(max_length=500)
    course = models.CharField(max_length=500)

    
    


    