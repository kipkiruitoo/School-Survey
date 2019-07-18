from django.contrib.postgres.fields import JSONField
from django.db import models

# Create your models here.


class Survey(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    visibility = models.CharField(max_length=255)
    allows_edit = models.CharField(max_length=255)
    identifier = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    form_builder_json = models.CharField(max_length=255)
    custom_submit_url = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Question(models.Model):
    title = models.CharField(max_length=300)
    help = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Answers(models.Model):
    answer = models.CharField(max_length=300)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer

class Questionaire(models.Model):
    title = models.CharField(max_length=300)
    showprogressbar = models.CharField(max_length=50)
    pages = JSONField()

    def __str__(self):
        return self.title

    
