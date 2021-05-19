from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=1000, verbose_name="Text", null=False)
    publication_date = models.DateField(verbose_name="Publication Date")

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    choice_text = models.CharField(max_length=200, verbose_name="Choice text", null=False)
    number_of_votes = models.IntegerField(verbose_name="Number of Votes", default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text
