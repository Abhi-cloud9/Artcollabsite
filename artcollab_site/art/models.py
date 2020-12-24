from ensurepip import version
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Skillset(models.Model):
    SKILL = (
        (u'D', u'Dance'),
        (u'M', u'Music'),
        (u'P', u'Photography'),
        (u'V', u'Videography'),
        (u'A', u'Art'),
        (u'O', u'Other')
    )
    skill = models.CharField(max_length=50, choices=SKILL, default='N/A')
    def __str__(self):
        return self.skill

class UserProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=0)
    gender_choices = (
        (u'M', u'Male'),
        (u'F', u'Female'),
        (u'O', u'Other'),
    )
    skill_set = models.ManyToManyField(Skillset)
    age = models.IntegerField()
    gender = models.CharField(max_length=6, choices=gender_choices, default='N/A')
    bio = models.TextField(max_length=400, blank=True)


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    country = models.CharField(max_length=50, default='N/A')
    state = models.CharField(max_length=50, default='N/A')
    city = models.CharField(max_length=50, default='N/A') 
    email = models.CharField(max_length=50, default='N/A')
    facebook_link = models.CharField(max_length=50, blank=True)
    instagram_link = models.CharField(max_length=50, blank=True)
    youtube_link = models.CharField(max_length=50, blank=True)
    other_sites = models.CharField(max_length=200, blank=True)
    phone = models.IntegerField()

