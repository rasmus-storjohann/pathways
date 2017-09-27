from django.contrib import admin
from .model import Choice, Question

admin.site.register(Question)
admin.site.register(Choice)
