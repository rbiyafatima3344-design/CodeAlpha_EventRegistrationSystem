from django.db import models
from django.contrib.auth.models import User
class Events(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    date=models.DateField()
    time=models.TimeField()
    location=models.CharField(max_length=200)
    available_seats=models.PositiveIntegerField()
    def __str__(self):
        return self.title
class Registration(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    event=models.ForeignKey(Events,on_delete=models.CASCADE)
    registered_at=models.DateTimeField(auto_now_add=True)
