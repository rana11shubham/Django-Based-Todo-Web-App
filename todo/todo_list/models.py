from django.db import models
from django.contrib.auth.models import User

class todo_elements(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    todo_title= models.CharField(max_length=200,null=True,blank=True)
    complete=models.BooleanField(default=False)
    create=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.todo_title