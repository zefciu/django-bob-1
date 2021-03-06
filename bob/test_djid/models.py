from django.db import models


class Person(models.Model):
    """Test person object reflecting the data from 
    http://www.briandunning.com/sample-data/"""
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    company_name = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    county = models.CharField(max_length=64)
    postal = models.CharField(max_length=64)
    phone1 = models.CharField(max_length=64)
    phone2 = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    web = models.CharField(max_length=64)
