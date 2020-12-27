from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    
    class Meta:
        ordering =('-created_date',)
        
    def __str__(self):
        return self.title