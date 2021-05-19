from django.db import models


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    email = models.CharField(max_length=200, verbose_name="Email Id")
    phone = models.CharField(max_length=10, verbose_name="Phone Number")
    message = models.TextField(verbose_name="Message", default="No Message")

    def __str__(self):
        return 'Message from ' + self.name + ' - ' + self.email
