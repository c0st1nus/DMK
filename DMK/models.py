from django.db import models

# Create your models here.
class lesson(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    subject = models.CharField(max_length=25)
