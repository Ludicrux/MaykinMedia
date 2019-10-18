# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class City(models.Model):
    city_name = models.CharField(max_length=50)
    city_abriviation = models.CharField(max_length=3)
    
    def __str__(self):
        return self.city_name

class Hotel(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    city_number = models.CharField(unique=True)
    hotel_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.hotel_name
    
    
    