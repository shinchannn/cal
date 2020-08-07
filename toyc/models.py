from django.db import models

class Record(models.Model):
    content = models.TextField(blank=True, null=True)
    posted_on = models.DateTimeField(auto_now_add=True)