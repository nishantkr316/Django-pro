from django.db import models

# Create your models here.
class IDCard(models.Model):
    card_number =models.CharField(max_length=50)

    def __str__(self):
        return self.card_number

class Subject(models.Model):
    name =models.CharField(max_length=50)

    def __str__(self):
        return self.name

class ClassRoom(models.Model):
    name =models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Student(models.Model):
    name=models.CharField(max_length=50)
    id_card =models.OneToOneField(IDCard,on_delete=models.CASCADE,related_name='student')
    classroom=models.ForeignKey(ClassRoom,on_delete=models.CASCADE,related_name='students')
    subject=models.ManyToManyField(Subject,related_name='students')
    def __str__(self):
        return self.name
