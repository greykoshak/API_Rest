from flask import Flask, jsonify, request

app = Flask(__name__)

client = app.test_client()  # Тестовый клиент Flask для тестирования приложения

tutorials = [
    {
        'title': 'Video #1. Intro',
        'description': 'GET, PUT routes'
    },
    {
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


if __name__ == '__main__':
    app.run()