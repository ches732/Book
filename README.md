# Справочник книг

Архитектура API - REST. 

Выполнено на Python с помощью фреймворков Django и DRF.

Хранимая информация о книгах:

* Заголовок книги;
* Автор книги: Имя, Фамилия, Отчество, Дата рождение, Дата смерти;
* Жанр книги: Наименование жанра;
* Цена книги;
* Год выпуска книги.

Описание API:

|           Действие            |                           URL                            | Метод  |         Параметры          |                                   Возвращаемый результат                                    | 
|:-----------------------------:|:--------------------------------------------------------:|--------|:--------------------------:|:-------------------------------------------------------------------------------------------:|
|          Вывод книги          |            http://127.0.0.1:8000/api/v1/book/            |  GET   |       Нет параметров       |                Результат операции (успех JSON с параметрами объекта, ошибка)                |
|       Добавление книги        |            http://127.0.0.1:8000/api/v1/book/            |  POST  | Json с параметрами объекта |                Результат операции (успех JSON с параметрами объекта, ошибка)                |
|        Удаление книги         |        http://127.0.0.1:8000/api/v1/book/<int:id>        | DELETE |       Нет параметров       |                             Результат операции (успех, ошибка)                              |
|     Редактирование книги      |        http://127.0.0.1:8000/api/v1/book/<int:id>        |  PUT   | Json с параметрами объекта |                Результат операции (успех JSON с параметрами объекта, ошибка)                |
| Получение авторов по id книги |    http://127.0.0.1:8000/api/v1/book/<int:id>/authors    |  GET   |       Нет параметров       |                Результат операции (успех JSON с параметрами объекта, ошибка)                |
|  Добавление авторов в книгу   |    http://127.0.0.1:8000/api/v1/book/<int:id>/authors    |  POST  | Json с параметрами объекта |                             Результат операции (успех, ошибка)                              |
|   Удаление авторов из книги   |    http://127.0.0.1:8000/api/v1/book/<int:id>/authors    | DELETE | Json с параметрами объекта |                             Результат операции (успех, ошибка)                              |
| Получение жанров по id книги  |    http://127.0.0.1:8000/api/v1/book/<int:id>/genres     |  GET   |       Нет параметров       |                Результат операции (успех JSON с параметрами объекта, ошибка)                |
|   Добавление жанров в книгу   |    http://127.0.0.1:8000/api/v1/book/<int:id>/genres     |  POST  | Json с параметрами объекта |                             Результат операции (успех, ошибка)                              |
|   Удаление жанров из книги    |    http://127.0.0.1:8000/api/v1/book/<int:id>/genres     | DELETE | Json с параметрами объекта |                             Результат операции (успех, ошибка)                              |
|  Получение всех авторов книг  |          http://127.0.0.1:8000/api/v1/authors/           |  GET   |       Нет параметров       |                Результат операции (успех JSON с параметрами объекта, ошибка)                |
|        Создание автора        |          http://127.0.0.1:8000/api/v1/authors/           |  POST  | Json с параметрами объекта |                Результат операции (успех JSON с параметрами объекта, ошибка)                |
|    Получение автора по id     |      http://127.0.0.1:8000/api/v1/authors/<int:pk>       |  GET   |       Нет параметров       |                Результат операции (успех JSON с параметрами объекта, ошибка)                |
|    Обновление автора по id    |      http://127.0.0.1:8000/api/v1/authors/<int:pk>       |  PUT   | Json с параметрами объекта |                Результат операции (успех JSON с параметрами объекта, ошибка)                |
|     Удаление автора по id     |      http://127.0.0.1:8000/api/v1/authors/<int:pk>       | DELETE |       Нет параметров       |                             Результат операции (успех, ошибка)                              |
|  Получение всех жанров книг   |           http://127.0.0.1:8000/api/v1/genres/           |  GET   |       Нет параметров       |                Результат операции (успех JSON с параметрами объекта, ошибка)                |
|        Создание жанра         |           http://127.0.0.1:8000/api/v1/genres/           |  POST  | Json с параметрами объекта |                Результат операции (успех JSON с параметрами объекта, ошибка)                |
|     Получение жанра по id     |       http://127.0.0.1:8000/api/v1/genres/<int:pk>       |  GET   |       Нет параметров       |                Результат операции (успех JSON с параметрами объекта, ошибка)                |
|    Обновление жанра по id     |       http://127.0.0.1:8000/api/v1/genres/<int:pk>       |  PUT   | Json с параметрами объекта |                Результат операции (успех JSON с параметрами объекта, ошибка)                |
|     Удаление жанра по id      |       http://127.0.0.1:8000/api/v1/genres/<int:pk>       | DELETE |       Нет параметров       |                             Результат операции (успех, ошибка)                              |

## Приложение 1 
Параметры для фильтрации книг
|           Параметр            |                 Назначение                |
|:-----------------------------:|:------------------------------------------|
|          title                |            Указывает заголовок книги      |
|          price_>              |            Указывает цену книги           |
|          genres               |            Указывает жанры книги          |
|          authors              |            Указывает авторов книги        |
|          release_year_<       |            Указывает год выпуска книги    |


Примечание

У параметров price, release_year могут быть постфиксы "_>" и "_<", что будет означать больше или меньше соответственно.

Пример

![2](https://github.com/ches732/Book/assets/102036166/ef4b7b50-eba9-4fd7-a66e-4739278fa674)


## Usage example
Запрос:

    POST /api/v1/book/ HTTP/1.1
    Host: 127.0.0.1:8000
    Content-Type: application/json
    
    {    
    "title": "Пеппи Длинныйчулок",
    "authors": [
        {
            "first_name": "Астрид",
            "last_name": "Линдгрен",
            "date_of_birth": "1868-04-01",
            "date_of_death":"1918-12-02"
        }
    ],
    "genres": [
        {
            "name":"Детская литература"
        }
    ],
    "price": 870,
    "release_year": 1948
    }

Ответ (в случае успеха):

    {
    "id": 1,
    "authors": [
        {
            "first_name": "Астрид",
            "last_name": "Линдгрен",
            "middle_name": null,
            "date_of_birth": "1868-04-01",
            "date_of_death": "1918-12-02"
        }
    ],
    "genres": [
        {
            "name": "Детская литература"
        }
    ],
    "title": "Пеппи Длинныйчулок",
    "price": 870,
    "release_year": 1948
    }

Запрос:

    GET /api/v1/book/ HTTP/1.1
    Host: 127.0.0.1:8000

Смотреть приложение 1.

Запрос:

    PUT /api/v1/book/1 HTTP/1.1
    Host: 127.0.0.1:8000
    Content-Type: application/json
    
    {    
    "title": "Пеппи Длинныйчулок",
    "authors": [
        {
            "first_name": "Ева",
            "last_name": "Линдгрен",
            "date_of_birth": "1868-04-01",
            "date_of_death":"1918-12-02"
        }
    ],
    "genres": [
        {
            "name":"Сказка"
        }
    ],
    "price": 900,
    "release_year": 1948
    }

Ответ (в случае успеха):

    {
    "id": 1,
    "authors": [
        {
            "first_name": "Ева",
            "last_name": "Линдгрен",
            "middle_name": null,
            "date_of_birth": "1868-04-01",
            "date_of_death": "1918-12-02"
        }
    ],
    "genres": [
        {
            "name": "Сказка"
        }
    ],
    "title": "Пеппи Длинныйчулок",
    "price": 900,
    "release_year": 1948
    }

Запрос:

    DELETE /api/v1/book/1 HTTP/1.1
    Host: 127.0.0.1:8000
    Content-Type: application/json
    
В случае успеха удаляется книга из БД

Запрос:
    
    GET /api/v1/book/1/authors HTTP/1.1
    Host: 127.0.0.1:8000
    Content-Type: application/json

Ответ (в случае успеха):   
    
    [
    {
        "first_name": "Астрид",
        "last_name": "Линдгрен",
        "middle_name": null,
        "date_of_birth": "1868-04-01",
        "date_of_death": "1918-12-02"
    }
    ]

Запрос:
    
    POST /api/v1/book/1/authors HTTP/1.1
    Host: 127.0.0.1:8000
    Content-Type: application/json

    {
    "author_ids": [2, 3]
    }
    
В случае успеха в книгу 1 добавятся авторы у которых id: 2, 3
При запросе GET /api/v1/book/1/authors будет:

    [
    {
        "first_name": "Астрид",
        "last_name": "Линдгрен",
        "middle_name": null,
        "date_of_birth": "1868-04-01",
        "date_of_death": "1918-12-02"
    },
    {
        "first_name": "Илья",
        "last_name": "Ильф",
        "middle_name": null,
        "date_of_birth": "1897-10-15",
        "date_of_death": "1937-04-13"
    },
    {
        "first_name": "Евгений",
        "last_name": "Петров",
        "middle_name": null,
        "date_of_birth": "1902-12-13",
        "date_of_death": "1942-07-02"
    }
    ]

Запрос:

    DELETE /api/v1/book/1/authors HTTP/1.1
    Host: 127.0.0.1:8000
    Content-Type: application/json
    
    {
        "author_ids": [2, 3]
    }
В случае успеха авторы с id: 2, 3 удалятся из книги

Запрос:

    GET /api/v1/book/1/genres HTTP/1.1
    Host: 127.0.0.1:8000
    Content-Type: application/json
    
Ответ:

    [
        {
            "name": "Детская литература"
        }
    ]

Запрос:

    POST /api/v1/book/1/authors HTTP/1.1
    Host: 127.0.0.1:8000
    Content-Type: application/json

    {
    "genre_ids": [2, 3]
    }
    
В случае успеха в книгу 1 добавится жанр у которого id: 2
При запросе GET /api/v1/book/1/authors будет:
    
    [
    {
        "name": "Детская литература"
    },
    {
        "name": "Роман"
    }
    ]

Запрос:

    DELETE /api/v1/book/1/authors HTTP/1.1
    Host: 127.0.0.1:8000
    Content-Type: application/json
    
    {
        "genre_ids": [2]
    }

В случае успеха жанр с id: 2 удалится из книги

Запрос:

    GET /api/v1/authors/ HTTP/1.1
    Host: 127.0.0.1:8000
    Content-Type: application/json

Ответ:

    [
    {
        "first_name": "Астрид",
        "last_name": "Линдгрен",
        "middle_name": null,
        "date_of_birth": "1868-04-01",
        "date_of_death": "1918-12-02"
    },
    {
        "first_name": "Илья",
        "last_name": "Ильф",
        "middle_name": null,
        "date_of_birth": "1897-10-15",
        "date_of_death": "1937-04-13"
    },
    {
        "first_name": "Евгений",
        "last_name": "Петров",
        "middle_name": null,
        "date_of_birth": "1902-12-13",
        "date_of_death": "1942-07-02"
    }
    ]

Запрос:
    
    POST /api/v1/authors/ HTTP/1.1
    Content-Type: application/json
    Host: 127.0.0.1:8000

    {
    "first_name": "Стефан",
    "last_name": "Цвейг",
    "date_of_birth": "1881-11-28",
    "date_of_death":"1942-02-22"
    }

Ответ:

    {
    "first_name": "Стефан",
    "last_name": "Цвейг",
    "middle_name": null,
    "date_of_birth": "1881-11-28",
    "date_of_death": "1942-02-22"
    }

Запрос:
    
    GET /api/v1/authors/1 HTTP/1.1
    Host: 127.0.0.1:8000
    Content-Type: application/json

Ответ:

    {
    "first_name": "Астрид",
    "last_name": "Линдгрен",
    "middle_name": null,
    "date_of_birth": "1868-04-01",
    "date_of_death": "1918-12-02"
    }

Запрос:
    
    PUT /api/v1/authors/1 HTTP/1.1
    Host: 127.0.0.1:8000
    Content-Type: application/json

    [
    {
        "first_name": "Ева",
        "last_name": "Лингред",
        "middle_name": null,
        "date_of_birth": "1890-11-28",
        "date_of_death": "1950-02-22"
    }
    ]

Ответ:

    [
    {
        "first_name": "Ева",
        "last_name": "Лингред",
        "middle_name": null,
        "date_of_birth": "1890-11-28",
        "date_of_death": "1950-02-22"
    }
    ]

Запрос:

    DELETE /api/v1/authors/3 HTTP/1.1
    Host: 127.0.0.1:8000

В случае успеха автор удалится полностью

Запрос:

    GET /api/v1/genres/ HTTP/1.1
    Host: 127.0.0.1:8000
    Content-Type: application/json

Ответ:

    [
    {
        "name": "Детская литература"
    },
    {
        "name": "Роман"
    }
    ]

Запрос:
    
    POST /api/v1/genres/ HTTP/1.1
    Content-Type: application/json
    Host: 127.0.0.1:8000

Ответ:
    
    {
        "name": "Фантастика"
    }

Запрос:

    GET /api/v1/genres/1 HTTP/1.1
    Content-Type: application/json
    Host: 127.0.0.1:8000

Ответ:

    [
    {
        "name": "Детская литература"
    }
    ]

Запрос: 
    
    PUT /api/v1/genres/1 HTTP/1.1
    Content-Type: application/json
    Host: 127.0.0.1:8000
    
    {
        "name": "Рассказ"
    }

Ответ:

    {
        "name": "Рассказ"
    }

Запрос:

    DELETE /api/v1/genres/3 HTTP/1.1
    Host: 127.0.0.1:8000

В случае успеха жанр удалится полностью
