from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    cnic = models.CharField(max_length=13)
    address = models.TextField()
    phone = models.IntegerField()

    def __str__(self):
        return str(self.name)
        
    
