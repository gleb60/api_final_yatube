# Api Yatube
## Технологии
- Python 3.9
- Django 3.2.16
- Djoser 2.2.0
- Django REST framework 3.12.4
- Библеотека для работы с JWT токенами simplejwt 4.7.2
## Описание проекта
Апи разработано для проекта YAtube.Благодаря этому проекту можно создавать посты, подписываться на авторов и комментировать посты.
Также можно создать свою страничку.Пользователь может смотреть все посты с пагинацией, подписываться на авторов и комментировать их записи.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:gleb60/api_final_yatube.git
```

```
cd kittygram
```

Cоздать виртуальное окружение на Linux:

```
python3 -m venv venv
```

Или на Windows:

```
python -m venv venv
```

И активировать виртуальное окружение:
```
source .venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

## Доступные эндпоинты

- api/v1/posts/ - получаем список всех постов или создаем новый пост.
- api/v1/posts/{post_id} - получаем, редактируем или удаляем пост.
- api/v1/posts/{post_id}/comments/ - получаем список комментариев к публикации или добавляем новый комментарий.
- api/v1/posts/{post_id}/comments/{id} - получаем/редактируем/удаляем конкретный комментарий конкретного поста по id.
- api/v1/groups/ - получаем список групп.
- api/v1/groups/{id} - получаем информацию о сообществе по id.
- api/v1/follow/ - получаем все подписки пользователя, сделавшего запрос или подписываемся на пользователя переданного в тело запроса.
Анонимные запросы запрещены. Возможен поиск по подпискам по параметру search.
- api/v1/jwt/create/ - создание JWT токена
- api/v1/jwt/refresh/ - обновление JWT токена
- api/v1/jwt/verify/ - проверка JWT токена

## Примеры запросов и ответов API
Пример POST запроса 
_.../api/v1/posts/_
```
{
    "text": "Первый пост"
}
```
Пример ответа:
```
{
    "id": 5,
    "author": "username",
    "text": "Первый пост",
    "pub_date": "2023-05-09T17:17:23.663450Z",
    "image": null,
    "group": null
}
```
Пример POST запроса 
_.../api/v1/posts/5/comments/_
```
{
    "text": "Первый комментарий"
}
```
Пример ответа:
```
{
    "id": 3,
    "author": "username",
    "text": "Первый комментарий",
    "created": "2023-05-09T17:24:40.398345Z",
    "post": 5
}
```

Пример GET запроса _.../api/v1/follow/_

Пример ответа:
```
{
    "user": "user",
    "following": "user1"
}
```