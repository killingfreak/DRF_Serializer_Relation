from django.db import models

# Create your models here.
class School(models.Model):
    school = models.CharField(max_length=50)
    def __str__(self):
        return self.school
    class Meta:
        ordering = ['id']


class Student(models.Model):
    student = models.CharField(max_length=30)
    roll = models.IntegerField()
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=False, max_length=30, related_name='student')
    def __str__(self):
        return self.student
    class Meta:
        ordering = ['roll']
