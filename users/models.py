from django.db import models
#User model provided by Django
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Users(models.Model):
    #Extending Django's User Model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    githubUsername = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=10, unique=True)
    institute = models.CharField(max_length=150, default='Institute')
    created_at = models.DateTimeField(default=timezone.now)

    #REFER THE DOCS for Accessing the Preset User Model by Django:-
    ### https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#extending-the-existing-user-model ###