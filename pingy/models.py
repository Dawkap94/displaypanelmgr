from django.db import models


class User(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Website(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.CharField(max_length=200)
    status = models.IntegerField(default=0)
    last_checked = models.IntegerField(default=0)
