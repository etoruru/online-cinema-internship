from django.contrib import admin

from .models import ConvertTask, Video

# Register your models here.
admin.site.register(Video)
admin.site.register(ConvertTask)
