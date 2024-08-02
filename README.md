# Написать на Python 2.7 небольшой сервис отправки имейл рассылок.


### Цели
 1. Отправка рассылок с использованием html макета и списка подписчиков.
 2. Отправка отложенных рассылок.
 3. Использование переменных в макете рассылки. (Пример: имя, фамилия, день рождения из списка подписчиков)
 4. Отслеживание открытий писем.
Отложенные отправки реализовать при помощи Celery


### Слово автора. 

Нашел интересную особенность. Celery запускал через Redis. Потратил несколько часов на изучение проблемы, которая возникала с редиской
<img src="https://github.com/Orwall46/task5/blob/master/DecodeError.PNG?raw=true" alt="Alt text" title="Optional title">
По итогу перешел на rabbitmq, там проблем не наблюдалось.

### Запуск проекта
```
git clone ...
```
Install dependencies, run virtual environment
```
python -m venv .venv
```
```
cd .venv/scripts
```
```
activate
```
```
pip install -r requirements.txt
``` 
Run Django, Rabbit, Celery
```
cd Mail
```
```
python manage.py runserver
```
```
docker run --rm -it --hostname my-rabbit -p 15672:15672 -p 5672:5672 rabbitmq:3-management
```
```
celery -A Mail.celeryapp worker --pool=solo -l info
```

На главной странице реализована обычная отправка сообщений без Celery. Мы тут передаем переменную в шаблон и отправляем клиентам. 
Для отправки отложенных писем - используйте раздел в меню "Отложенная отправка"

Админ панель доступна по адресу http://127.0.0.1/admin/ для добавления новых пользователей и отслеживания прочтения письма.
