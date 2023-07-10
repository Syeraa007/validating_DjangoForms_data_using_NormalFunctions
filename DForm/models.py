from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    cls=models.IntegerField()
    loc=models.CharField(max_length=100)
    email=models.EmailField()

    def __str__(self) -> str:
        return self.name