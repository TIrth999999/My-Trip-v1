from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length = 122,default = "NULL")
    email = models.CharField(max_length = 122,default = "NULL")
    subject = models.CharField(max_length = 10,default = "NULL")
    message = models.CharField(max_length = 1000,default = "NULL")

    def __str__(self):
        return self.name
    
class Review(models.Model):
    name = models.CharField(max_length = 122,default = "NULL")
    city = models.CharField(max_length = 122,default = "NULL")
    trip = models.CharField(max_length = 10,default = "NULL")
    star = models.CharField(max_length = 1000,default = "NULL")
    message = models.CharField(max_length = 1000,default = "NULL")
    
    def __str__(self):
        return self.name
    
class Package(models.Model):
    image = models.ImageField(default="static/img/gujarat-1.jpg")
    name = models.CharField(max_length = 122,default = "NULL")
    city = models.CharField(max_length = 122,default = "NULL")
    star = models.IntegerField(max_length = 5,default = 5)
    days = models.IntegerField(max_length = 100,default = 2)
    person = models.IntegerField(max_length = 99,default = 4)
    price = models.IntegerField(max_length=999999,default=10000)

    def __str__(self):
        return self.name