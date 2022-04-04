from django.db import models


# Create your models here.
class Todo(models.Model):
    body=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)
    is_completed=models.BooleanField(default=False)

    def __str__(self):
       return self.body
   

