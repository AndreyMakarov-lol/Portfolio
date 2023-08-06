from django.urls import path
from . import views
#Подключаем наш шаблон
urlpatterns = [path('', views.PostView.as_view())]