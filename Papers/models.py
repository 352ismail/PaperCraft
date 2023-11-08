from django.db import models

# Create your models here.

class Paper(models.Model):
    Title = models.CharField(max_length=100)
    Subject = models.CharField(max_length=80)
    Duration = models.IntegerField()
    Instructions = models.TextField(null=True)
    TotalMarks = models.IntegerField(default=0)
    TeacherName = models.CharField(max_length=100)
    Class = models.CharField(max_length=50)

    def __str__ (self):
        return f'{self.Title} {self.Subject}'