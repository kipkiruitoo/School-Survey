from django.contrib import admin
from .models import Survey
from .models import Category
from .models import Questionaire
# Register your models here.
admin.site.register(Survey)
admin.site.register(Category)
admin.site.register(Questionaire)

