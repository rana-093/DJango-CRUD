from django.db import models

# Create your models here.


class Position(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Employee(models.Model):
    fullName = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=4)
    mobile = models.CharField(max_length=11)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
