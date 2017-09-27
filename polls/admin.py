from django.contrib import admin
from . import model

admin.site.register(model.Question)
admin.site.register(model.Choice)
