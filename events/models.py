from django.db import models
from django.utils import timezone
# Create your models here.

class Participant(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    def __str__(self):
        return self.name
    
class Category(models.Model):
    name=models.CharField(max_length=200,unique=True)
    description=models.TextField(blank=True,null=True)
    def __str__(self):
        return self.name
    
class Event(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField(blank=True,null=True)
    start_date=models.DateField(default=timezone.now)
    end_date=models.DateField(default=timezone.now)
    time=models.TimeField(blank=True,null=True)
    location=models.CharField(max_length=300)

    category = models.ForeignKey(
        Category,
        blank=False,
        on_delete=models.CASCADE,
        related_name='events')
    participants = models.ManyToManyField(
        Participant,
        related_name='events',
        blank=True,
     )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name 
    
    
    
