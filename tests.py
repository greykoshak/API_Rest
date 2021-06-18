from app import client


def test_simple():
    mylist = [1, 2, 3, 4, 5]

    assert 3 in mylist


def test_get():
    res = client.get('/tutorials')
    assert res.status_code == 200
    assert len(res.get_json()) == 2
    assert res.get_json()[0]['id'] == 1


def test_post():
    data = {
        'id': 3,
        'title': 'Test',
        'description': 'Testing POST route'
    }
    res = client.post('/tutorials', json=data)
    assert res.status_code == 200
    assert len(res.get_json()) == 3
    assert res.get_json()[-1]['id'] == 3
    assert res.get_json()[-1]['title'] == data['title']


def test_put():
    data = {
        'id': 2,
        'description': 'Testing PUT route'
    }
    res = client.put('/tutorials/2', json=data)
    assert res.status_code == 200
    assert len(res.get_json()) == 3
    assert res.get_json()[1]['description'] == data['description']


def test_delete():
    res = client.delete('/tutorials/1')
    assert res.status_code == 204
    res = client.get('/tutorials')
    assert len(res.get_json()) == 2
