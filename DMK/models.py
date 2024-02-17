from django.db import models

# Create your models here.
class Step(models.Model):
    description = models.CharField(max_length=25)
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE, related_name='step_lesson', default=1)

class Lesson(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    subject = models.CharField(max_length=25)
    description = models.CharField(max_length=25, default='Default description')
    steps = models.ManyToManyField(Step, related_name='lesson_steps')
    test = models.CharField(max_length=25)