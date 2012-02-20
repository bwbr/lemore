# -*- coding: utf-8 -*-
from django.contrib.auth.models import User

from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=60)
    createon = models.DateField(auto_now_add=True)
    leader = models.ForeignKey('Author', blank=True, null=True)

class Author(User):
    mugen_group = models.ForeignKey('Group')
