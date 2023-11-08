from django.db import models
from Papers.models import Paper

class PaperTemplate(models.Model):
    Exam = models.CharField(max_length=100)
    ShortQuestions = models.IntegerField(null=True)
    LongQuestions = models.IntegerField(null=True)
    FillIntheBlanks = models.IntegerField(null=True)
    MCQs = models.IntegerField(null=True)
    TrueFalse = models.IntegerField(null=True)
    ExtraFileds = models.CharField(max_length=200, null=True)
    Paper = models.ForeignKey(Paper, related_name='paper' , on_delete=models.CASCADE)