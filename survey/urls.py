
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('surveys', views.SurveyView)
router.register('categories', views.CategoryView)
# router.register('categories/<int:pk>/', views.CategoryView)
# router.register('question', views.QuestionView)
# router.register('answers', views.AnswersView)
router.register('questionaires', views.QuestionaireView)
# router.register('question', views.QuestionView)
router.register('answers', views.AnswersView)

urlpatterns = [

    path('', include(router.urls)),
    path('auth-login', include('rest_framework.urls'))

]
