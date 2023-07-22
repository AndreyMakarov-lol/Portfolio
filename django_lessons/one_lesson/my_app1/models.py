from django.db import models
from django.db.models import CharField


# Создаем класс таблицы нашей БД
class Worker(models.Model):
    name = models.CharField(max_length=20, blank=False)  # Создаём столбец name со
    # строковым типом данных (CharField), максимальной длинной 20 символов (max_length=20), запретом на пустое поле(
    # blank=False)
    second_name: CharField = models.CharField(max_length=35, blank=False)  # Создаём столбец second_name аналогично предидущему
    salary = models.IntegerField(default=0)  # Создаём столбец salary с числовым типом данных
    # с начальным значением 0
    def __str__(self):
        return f'{self.second_name} {self.name}'