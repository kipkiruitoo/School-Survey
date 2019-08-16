from rest_framework import serializers
from .models import Survey
from .models import Category

from .models import Answers, Questionaire


class SurveySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Survey
        fields = ('id', 'url', 'name', 'description')

# class QuestionSerializer(serializers.HyperlinkedModelSerializer):

#     class Meta:
#         model = Question
#         fields = ('id', 'url', 'title', 'help', 'category')


class AnswersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answers
        fields = ('id', 'school', 'answer', 'category')


class QuestionaireSerializer(serializers.ModelSerializer):
    pages = serializers.JSONField()  # change is here

    class Meta:
        model = Questionaire
        fields = ('id', 'pages', 'category')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    questionaire = QuestionaireSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'description', 'questionaire')
