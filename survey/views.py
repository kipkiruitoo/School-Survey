from django.shortcuts import render
from rest_framework import permissions
from rest_framework import viewsets, mixins, generics
from .models import Survey, Category, Answers, Questionaire
from .serializers import (SurveySerializer, CategorySerializer,
                          AnswersSerializer, QuestionaireSerializer)
from rest_framework import viewsets
# from .models import Survey, Category, Question, Answers
from .serializers import SurveySerializer, CategorySerializer,  AnSerializer, AnswersSerializer
from rest_framework.response import Response


# Create your views here.


class SurveyView(viewsets.ModelViewSet):

    permission_classes = (permissions.AllowAny,)

    queryset = Survey.objects.all()
    serializer_class = SurveySerializer


class CategoryView(viewsets.ModelViewSet):

    permission_classes = (permissions.AllowAny,)

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# class QuestionView(viewsets.ModelViewSet):
#     queryset = Question.objects.all()
#     serializer_class = QuestionSerializer


class AnswersView(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Answers.objects.all()
    serializer_class = AnswersSerializer


class QuestionaireView(viewsets.GenericViewSet, generics.RetrieveUpdateDestroyAPIView, generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = Questionaire.objects.all()
    serializer_class = QuestionaireSerializer
    lookup_field = 'category'


class AnsView(viewsets.ModelViewSet):
    # permission_classes = (permissions.AllowAny,)
    queryset = Answers.objects.all()
    serializer_class = AnswersSerializer
    # lookup_field = 'category'

    def retrieve(self, request, pk=None):
        pk = pk
        queryset = Answers.objects.filter(category=pk)
        serializer = AnSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)
