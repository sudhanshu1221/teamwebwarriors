from django.db import models


# Create your models here.


class Feedback(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    email = models.CharField(max_length=200, verbose_name="Email Id")
    rating = models.CharField(max_length=1, verbose_name="Rating")
    feedback = models.TextField(verbose_name="Feedback", default="No Feedback")

    def __str__(self):
        return 'Feedback from ' + self.name + ' - ' + self.rating + '/5'
