from django.db import models

# Create your models here.


class Doctor(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Patient(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Appoinment(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE,related_name='appoinments')
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE,related_name='appoinments')
    date=models.DateField()


