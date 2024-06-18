from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name=models.CharField(max_length=25)
    age=models.IntegerField()
    photo=models.ImageField(upload_to='media/')
