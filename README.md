# Тестовое задание для студии "INDEX"
![Workflow](https://github.com/istillmissyou/test_guru/actions/workflows/test_guru_workflow.yaml/badge.svg)

Проекто запущен на сервере
![Доступ](http://158.160.11.215/)

## Автор

Штунь Данил

## Описание

* **GET /city/** — получение всех городов из базы
* **POST /city/** — создание города
* **GET /city/city_id/street/** —  получение всех улиц города; (city_id —
идентификатор города)
*  **POST /city/city_id/street/** —  создание улицы в городе; (city_id —
идентификатор города)
* **POST /shop/** —  создание магазина; Данный метод получает json c
объектом магазина, в ответ возвращает данные созданной записи
* **GET /shop/?street=&city=&open=0/1** — получение списка магазинов.
I. Метод принимает параметры для фильтрации. Параметры не обязательны. В
случае отсутствия параметров выводится все магазины, если хоть один параметр
есть, то по нему выполнятся фильтрации.
II. Важно! В объекте каждого магазина выводится название города и улицы, а не id
записей.
III. Параметр open: 0 - закрыт, 1 - открыт. Данный статус определяет исход из
параметров «Врем открытия», «Врем закрытия» и текущего времени сервера.

## Использованные технологии

* Python 3.10
* Django 4.1.2
* Django Rest Framework 3.14.0
* Simple-JWT 4.8.0
* Gunicorn 20.1.0

## Запуск dev-сервера

Клонировать проект 

```
git clone https://github.com/istillmissyou/test_guru.git
```

Установить Docker

```
sudo apt install docker.io
```

```
sudo apt install docker-compose
```


### Шаблон наполнения env-файла

```
DB_ENGINE=указываем, что работаем с postgresql
DB_NAME=имя базы данных
POSTGRES_USER=логин для подключения к базе данных
POSTGRES_PASSWORD=пароль для подключения к БД (установите свой)
DB_HOST=название сервиса (контейнера)
DB_PORT=порт для подключения к БД 
```

### Как запустить проект:

Клонировать репозиторий и перейти в директорию "infra" открыть файл docker-compose.yaml и в 11 строке поменять `image: ssd256/test_guru` на `build: .` Дальше в командной строке:

```
sudo docker-compose up
```

Проект запущен!

