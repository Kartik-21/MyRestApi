from django.contrib import admin

# Register your models here.
from .models import UserPost, ShowPost


# admin.site.register(UserPost)

@admin.register(UserPost)
class UserPostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'time']


@admin.register(ShowPost)
class ShowPostAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'time']
