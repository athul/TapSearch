from django.db import models

# Create your models here.
class query(models.Model):
    S_query=models.TextField()
class Document(models.Model):
    doc=models.CharField(max_length=500)