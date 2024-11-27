from django.db import models
import datetime
# Create your models here.
class Record(models.Model):
    Created=models.DateTimeField(auto_now_add=True,)
    username=models.CharField(max_length=50)
    email=models.EmailField()
    PhNo=models.CharField(max_length=10)

