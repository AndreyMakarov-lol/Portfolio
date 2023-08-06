from django.shortcuts import render
from django.views.generic.base import View

# Представление вывода записей

# Импортируем модель данных
from .models import Posts

class PostView(View):
    """Вывод записей"""
    def get(self, request):
        posts = Posts.objects.all()
        return render(request, 'blog/blog.html', {"post_list": posts})
