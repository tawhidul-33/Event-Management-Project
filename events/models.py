from django.db import models
# Create your models here.

class Participant(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(unique=True)
    events= models.ManyToManyField(
        "Event",
        related_name="participants",

    )
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
    data=models.DateField()
    time=models.TimeField()
    locationn=models.CharField(max_length=300)
    category= models.ForeignKey(# ForeignKey to Category (One category → Many events)
        Category,
        on_delete=models.CASCADE,
        related_name="events"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name 
    
