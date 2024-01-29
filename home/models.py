# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Userprofile(models.Model):

    #__Userprofile_FIELDS__
    username = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    userid = models.CharField(max_length=255, null=True, blank=True)
    contactid = models.CharField(max_length=255, null=True, blank=True)

    #__Userprofile_FIELDS__END

    class Meta:
        verbose_name        = _("Userprofile")
        verbose_name_plural = _("Userprofile")


class Contact(models.Model):

    #__Contact_FIELDS__
    contactid = models.CharField(max_length=255, null=True, blank=True)
    creatoruserid = models.CharField(max_length=255, null=True, blank=True)

    #__Contact_FIELDS__END

    class Meta:
        verbose_name        = _("Contact")
        verbose_name_plural = _("Contact")


class Processes(models.Model):

    #__Processes_FIELDS__
    processid = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    creatoruserid = models.CharField(max_length=255, null=True, blank=True)

    #__Processes_FIELDS__END

    class Meta:
        verbose_name        = _("Processes")
        verbose_name_plural = _("Processes")



#__MODELS__END
