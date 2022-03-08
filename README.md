# Загрузка фото NASA

Данный скрипт позволяет загружать фотографии с сервисов [NASA EPIC](https://api.nasa.gov/#epic) и [NASA APOD](https://api.nasa.gov/#apod), а также фотографии [последнего запуска SPACEX](https://documenter.getpostman.com/view/2025350/RWaEzAiG#bc65ba60-decf-4289-bb04-4ca9df01b9c1)

### Как установить

Для начала работы необходимо зарегистрироваться на [сайте NASA](https://api.nasa.gov/) и сгенерировать токен.

Далее, в папке со скриптом необходимо создать файл `.env` и записать в него токен в виде `NASA_API_KEY=ваш_токен`

[Python3](https://www.python.org/downloads/) должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).