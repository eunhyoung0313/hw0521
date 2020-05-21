from django.db import models

class Todolist(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    duedate=models.TextField()

    def __str__(self):
        return self.title
# Create your models here.
