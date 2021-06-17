from flask import Flask, jsonify, request

app = Flask(__name__)

client = app.test_client()  # Тестовый клиент Flask для тестирования приложения

tutorials = [
    {
        'id': 1,
        'title': 'Video #1. Intro',
        'description': 'GET, PUT routes'
    },
    {
        'id': 2,
        'title': 'Video #2. More features',
        'description': 'UPDATE, DELETE routes'
    }
]


@app.route('/')
def index():
    return 'REST API: GET PUT UPDATE DELETE'''


@app.route('/tutorials', methods=['GET'])
def get_list():
    return jsonify(tutorials)


@app.route('/tutorials', methods=['POST'])
def update_list():
    new_one = request.json   # Получить данные, отправленные клиентом на расширение списка
    tutorials.append(new_one)
    return jsonify(tutorials)


@app.route('/tutorials/<int:tutorial_id>', methods=['PUT'])
def update_tutorial(tutorial_id):
    item = next((x for x in tutorials if x['id'] == tutorial_id), None)
    params = request.json   # Получить параметры, переданные для изменения

    if not item:
        return {'message': 'No tutorials with this id'}, 400
    item.update(params)  # item - элемент словаря
    return jsonify(tutorials)


@app.route('/tutorials/<int:tutorial_id>', methods=['DELETE'])
def delete_tutorial(tutorial_id):
    idx, _ = next((x for x in enumerate(tutorials) if x[1]['id'] == tutorial_id), (None, None))
    tutorials.pop(idx)
    return '', 204


if __name__ == '__main__':
    app.run()
