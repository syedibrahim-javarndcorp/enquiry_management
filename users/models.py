from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


# Create your models here.


class Profile(models.Model):
    USER_TYPE = (
        ('student', 'Student'),
        ('user', 'User'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100)
    username = models.CharField(max_length=100, blank=True, null=True)
    user_type = models.CharField(max_length=150, choices=USER_TYPE, default="student", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.user.username)


