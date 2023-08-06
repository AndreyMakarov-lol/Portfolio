from django.contrib import admin
from .models import Posts

# Регистрируем нашу мадель и настраиваем её отображение в админ панели

@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
