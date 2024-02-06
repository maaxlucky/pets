from django.db import models


# I make model Adopters and create database with adopters so I can call them and they can adopt pet
class Adopters(models.Model):
    name = models.CharField(max_length=20, blank=False)
    second_name = models.CharField(max_length=35, blank=False)
    email_address = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    pet_adopt = models.CharField(max_length=20, blank=False)
    info_additional = models.TextField()

    # Return some data from object
    def __str__(self):  # What means __?? Have to find what it means
        return f'{self.name} {self.second_name} {self.pet_adopt}'


# My first model Workers
class Worker(models.Model):
    name = models.CharField(max_length=20, blank=False)
    second_name = models.CharField(max_length=35, blank=False)
    salary = models.IntegerField(default=0)

    def __str__(self):
        return f' {self.second_name} {self.name}'

# Create your models here.
