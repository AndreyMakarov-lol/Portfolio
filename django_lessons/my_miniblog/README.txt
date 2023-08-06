Создаем проект в джанго командой: django-admin startproject one_lesson

Переходим в терминале в папку нажего веб-приложения: cd .....

Запускаем наже веб- приложение: ./manage.py runserver (для остановки зажимаем ^C)

Создаём миграцию базы данных нашего приложения: ./manage.py migrate

Создаём приложение внутри нашего веб-приложения: ./manage.py startapp my_app1

Для проведения миграции данных сначала: ./manage.py makemigrations
и после успешного завершения ./manage.py migrate
Создание суперюзера(админа) ./manage.py createsuperuser
