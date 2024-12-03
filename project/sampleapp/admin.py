from .imports.admin import BaseModelAdmin as Parent

from django.contrib import admin

from .models import NewModel as NewModelModel


@admin.register(NewModelModel)
class NewModelModelAdmin(Parent):
    list_display = ['id', ]
