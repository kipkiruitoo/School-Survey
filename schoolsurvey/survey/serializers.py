from rest_framework import serializers
from .models import Survey
from .models import Category
from .models import Answers, Questionaire


class SurveySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Survey
        fields = ('id', 'url', 'name', 'description')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'url', 'name', 'survey', 'visibility', 'allows_edit',
                  'identifier', 'description', 'form_builder_json', 'custom_submit_url')


class QuestionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Question
        fields = ('id', 'url', 'title', 'help', 'category')


class AnswersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answers
        fields = ('id', 'url', 'school', 'answer', 'questionId')

class QuestionaireSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Questionaire
        fields = '__all__'
