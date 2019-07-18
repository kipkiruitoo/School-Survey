from django.contrib.postgres.fields import JSONField
from django.db import models
from users.models import School

# Create your models here.


class Survey(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    #VSCode will see the objects declared
    objects = models.Manager()
    


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

    #VSCode will see the objects declared
    objects = models.Manager()
    



class Answers(models.Model):
    school = models.ForeignKey(School, related_name='answers', on_delete=models.CASCADE)
    questionId = models.CharField(max_length=250)
    answer = models.CharField(max_length=300)

    def __str__(self):
        return self.answer

    #VSCode will see the objects declared
    objects = models.Manager()
    

class Questionaire(models.Model):
    category = models.ForeignKey(Category, related_name='questionaire', on_delete=models.CASCADE)
    pages = JSONField()

    #VSCode will see the objects declared
    objects = models.Manager()
    

    
