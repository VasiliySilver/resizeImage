from django.contrib import admin

# Register your models here.
from .models import *


class ImageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"id": ("title",)}  # предварительно заполненные поля


admin.site.register(Image, ImageAdmin)
