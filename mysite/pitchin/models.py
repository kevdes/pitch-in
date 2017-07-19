# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Facility(models.Model):

    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'facilities'

# class User(models.Model):

#     name = models.CharField(max_length=200)
#     facility = models.ForeignKey('Facility')



# class Pitch(models.Model):

#     title = models.CharField(max_length=200)
#     summary = models.TextField()
#     created_date = models.DateTimeField()

#     users = models.ManyToManyField(User)


# class PitchStatus(models.Model):

#     name = models.CharField(max_length=100)


# class Category(models.Model):

#     name = models.CharField(max_length=200)



# class Post(models.Model):
#     author = models.ForeignKey('auth.User')
#     title = models.CharField(max_length=200)
#     text = models.TextField()
#     created_date = models.DateTimeField(
#             default=timezone.now)
#     published_date = models.DateTimeField(
#             blank=True, null=True)

#     def publish(self):
#         self.published_date = timezone.now()
#         self.save()

#     def __str__(self):
#         return self.title