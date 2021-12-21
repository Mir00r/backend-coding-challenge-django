from django.db import models
from django.db.models.fields import UUIDField


class Todo(models.Model):
    id = models.UUIDField(editable=False, unique=True, auto_created=True, primary_key=True)
    title = models.CharField(max_length=200)
    body = models.TextField(default='')
    tags = models.TextField()

    def __str__(self):
        return self.title