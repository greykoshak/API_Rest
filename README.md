# API_Rest
Реализация технологии API Rest на фреймворке Flask

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
    
    >>>res = client.post('/tutorials', json={'title': 'Video #4', 'decription': 'Unit tests'})
    >>>res.status_code
    >>>200
    >>>res.get_json()
    
    >>>res = client.put('/tutorials/2', json= {'description': 'Add PUT', 'title': 'Video #2. PUT'})
