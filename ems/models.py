from django.db import models
from users.models import Profile

# Create your models here.
class Ems(models.Model):
    owner = models.ForeignKey(Profile,null=True,blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    tag = models.ManyToManyField('Tag', blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'UP'),
        ('down', 'DOWN'),
    )
    # owner =
    project = models.ForeignKey(Ems, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=150, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.value


class Tag(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name
