# API_Rest
Реализация технологии API Rest на фреймворке Flask

https://www.youtube.com/watch?v=w8O6apM3aBw
https://www.youtube.com/watch?v=_pK0aUPpX_Q&list=PLWQhUNXl0LnjBIaE72hq1RkDsbWWSgeUr

#########################
Задача: Написать REST API
#########################

Ключевая информация:

    1. В REST API используют 4 основных вида http-запросов:
        GET
        PUT
        UPDATE
        DELETE
    2. Обычно при каждом запросе, который клиент отправляет серверу, 
    происходит идентификация пользователя посредством токена,
    который присутствует, например, в заголовке http-запроса.
    
    Используем flask-фреймворк
    
    Тестирование методов.
    ---------------------
    Terminal --> Python --> from app import app, client 
    >>>res = client.get('/tutorials')
    >>> res.get_json()
    >>>[{'description': 'GET, PUT routes', 'title': 'Video #1. Intro'}, {'description': 'UPDATE, DELETE routes', 'title': 'Video #2. More features'}]
    
    >>>res = client.post('/tutorials', json={'title': 'Video #4', 'decription': 'Unit tests', 'id': 4})
    >>>res.status_code
    >>>200
    >>>res.get_json()
    
    >>>res = client.put('/tutorials/2', json= {'description': 'Add PUT', 'title': 'Video #2. PUT'})
    
    >>>res = client.delete('/tutorials/1')
    >>>res.status_code
    >>>204
    >>>res = client.get('/tutorials')
    >>>res.get_json()
[{'description': 'UPDATE, DELETE routes', 'id': 2, 'title': 'Video #2. More features'}]

