# Постановка задачи

Необходимо реализовать дополнительный функционал в рамках [эталонного проекта](https://devel.mephi.ru/aialeksandrov/filmbase2024) «Каталог фильмов».
**Задание №7.6** Реализовать возможность персональной настройки отображения содержимого сайта.

## Проектирование моделей

![Wagtail class diagram](myapp_models.png)

## Запуск проекта

~~~cmd
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py import_films
python manage.py runserver
~~~

## Для построения диаграммы классов:

~~~cmd
python manage.py graph_models -a --dot -o myapp_models.dot; dot -Tpng myapp_models.dot -omyapp_models.png; rm -rf myapp_models.dot
~~~

# Изменения

1. **Настройка языка**: Позволяет выбрать предпочтительный язык интерфейса сайта.
   
2. **Тема оформления**: Позволяет выбрать светлую или темную тему оформления сайта в зависимости от предпочтений пользователя.

3. **Уведомления и оповещения**: Позволяет настраивать способы получения уведомлений.

4. **Настройка конфиденциальности**: Позволяет управлять уровнем конфиденциальности данных, выбирать, какие данные хранить и какие делиться с другими пользователями.