from django.contrib import admin

from .models import Bookmark, Comment, History, Subscription

# Register your models here.
admin.site.register(Comment)
admin.site.register(Subscription)
admin.site.register(History)
admin.site.register(Bookmark)
