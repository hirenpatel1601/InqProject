from django.db import models


# Create your models here.
class Contact(models.Model):
    email=models.CharField(max_length=122)
    StudentFirstName=models.CharField(max_length=122)
    StudentMidleName=models.CharField(max_length=122)
    StudentLastName=models.CharField(max_length=122)
    StudentMobile=models.CharField(max_length=13)
    ParentFirstName=models.CharField(max_length=122)
    ParentMidleName=models.CharField(max_length=122)
    ParentLastName=models.CharField(max_length=122)
    ParentMobile=models.CharField(max_length=13)
    Adress=models.TextField()
    Selection=models.CharField(max_length=50)
    Question=models.TextField()
    date=models.DateField()


def __str__(self):
    return self.name
