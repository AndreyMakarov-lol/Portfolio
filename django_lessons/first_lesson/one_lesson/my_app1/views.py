from django.shortcuts import render
from .models import Worker


def index_page(request):


    # Отобразить всех работников


    # Создаём новый объект с данными навого работника
    # new_worker = Worker(name='Иван', second_name='Кукин', salary=70000)
    # Сохраняет нового пользователя
    # new_worker.save()
    # worker_to_change = Worker.objects.get(id=5)#достаём нужную строку
    # worker_to_change.second_name = 'jopin'#меняем данные
    # worker_to_change.save()#сохраняем новые данные
    # Выводит все записи из базы данных в консоль при обновлении страницы
    people = Worker.objects.all()
    # Worker.objects.get(id=5).delete()#Удаление записи
    # print(people)
    # Выводит записи соответствующие условию фильтрации
    # из базы данных в консоль при обновлении страницы
    # filtr_people = Worker.objects.filter(salary=60000)
    # print(filtr_people)
    # Выводит все перечисленные данные
    # из базы данных в консоль при обновлении страницы
    # for i in people:
    #    print(f'Familia:{i.second_name}, Name:{i.name}, Zarplata:{i.salary}, id:{i.id}')

    return render(request, 'index.html', context={'data': people})


def about_page(request):
    return render(request, 'about.html')
