from django.shortcuts import render
from rest_framework import viewsets, mixins, generics
from .models import Survey, Category, Answers, Questionaire
from .serializers import (SurveySerializer, CategorySerializer, QuestionSerializer,
                 AnswersSerializer, QuestionaireSerializer)

# Create your views here.


class SurveyView(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# class QuestionView(viewsets.ModelViewSet):
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer



class AnswersView(viewsets.ModelViewSet):
    queryset = Answers.objects.all()
    serializer_class = AnswersSerializer

class QuestionaireView(viewsets.GenericViewSet, generics.RetrieveUpdateDestroyAPIView,generics.ListCreateAPIView):
                        
    queryset = Questionaire.objects.all()
    serializer_class = QuestionaireSerializer