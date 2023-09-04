from django.db import models

class Tasks(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    desc = models.TextField()