from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20)
    group = models.IntegerField()

    def __str__(self):
        return 'name: ' + str(self.name) + ', group: ' + str(self.group)

class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=20)
    description = models.CharField(max_length=500)
    current_student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True,
            null = True)

    def __str__(self):
        return 'id: '+ str(self.id) + ', ' +  'name: ' + str(self.name) + ', author: ' + str(self.author) + ', description: ' + str(self.description)

