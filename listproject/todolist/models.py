from django.db import models
from django.contrib.auth.models import User

class Todolist(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField(null="True")
    duedate=models.TextField(null="True")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title

class Comment(models.Model):
    post=models.ForeignKey(Todolist, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='comments')
    content=models.TextField(null="True")

    def __str__(self):
        return self.post
# Create your models here.
