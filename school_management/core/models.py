from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.PositiveIntegerField(unique=True)
    address = models.TextField()
    course = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.name} ({self.roll_no})"


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name
