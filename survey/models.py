
from django.contrib.postgres.fields import JSONField
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields.jsonb import JSONField as JSONBField
from django.db import models
from users.models import User


# Create your models here.


class Survey(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    # VSCode will see the objects declared
    objects = models.Manager()


class Category(models.Model):
    name = models.CharField(max_length=50)
    # survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    # visibility = models.CharField(max_length=255)
    # allows_edit = models.CharField(max_length=255)
    # identifier = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    # form_builder_json = models.CharField(max_length=255)
    # custom_submit_url = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    # VSCode will see the objects declared
    objects = models.Manager()


DEFAULT_CATEGORY_ID = 6


class Answers(models.Model):
    school = models.ForeignKey(
        User, related_name='answers', on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, related_name='answers', on_delete=models.CASCADE, default=DEFAULT_CATEGORY_ID)
    answer = JSONBField(default=list, null=True, blank=True)

    def __str__(self):
        return self.answer

    # VSCode will see the objects declared
    objects = models.Manager()


class Questionaire(models.Model):
    category = models.ForeignKey(Category, related_name='questionaire',
                                 on_delete=models.CASCADE, default=DEFAULT_CATEGORY_ID)
    # pages =  ArrayField(models.CharField(max_length=10485758))
    pages = JSONBField(default=list, null=True, blank=True)

    # VSCode will see the objects declared
    objects = models.Manager()

# ArrayField(models.CharField(max_length=10485758))


# class Question(models.Model):
#     title = models.CharField(max_length=300)
#     help = models.CharField(max_length=250)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title


# class Answers(models.Model):
#     answer = models.CharField(max_length=300)
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.answer
# >>>>>>> cf263849322247aab8b3cd232ec75db274f5cd70
