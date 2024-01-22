import json
from query import query_text_data, query_2ea_text_data, query_id_data
from response import response_skill_data, response_skill_condition_data, response_card_data
from flask import Flask, Response
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return Response('Hello World!', content_type='text/plain; charset=utf-8', status=200)

@app.route('/skill', methods=['POST'])
def get_skill_data():
    req = request.get_json()
    message = req['action']['params']['name']

    result = query_text_data(message, 'skill.sql')
    response = response_skill_data(result)
    response = json.dumps(response, ensure_ascii=False).encode('utf8')
    return Response(response, content_type='application/json; charset=utf-8', status=200)

@app.route('/skill_condition', methods=['POST'])
def get_skill_condition_data():
    req = request.get_json()
    skill_id = req['action']['clientExtra']['skill_id']
    if skill_id is None:
        return Response('Not found', content_type='text/plain; charset=utf-8', status=200)

    result = query_id_data(skill_id, 'skill_condition.sql')
    response = response_skill_condition_data(result)
    response = json.dumps(response, ensure_ascii=False).encode('utf8')
    return Response(response, content_type='application/json; charset=utf-8', status=200)

@app.route('/card', methods=['POST'])
def get_card_data():
    message = str()
    req = request.get_json()
    if 'name' in req['action']['params'] and req['action']['params']['name'] != '':
        message = req['action']['params']['name']
    elif 'name' in req['action']['clientExtra'] and req['action']['clientExtra']['name'] != '':
        message = req['action']['clientExtra']['name']

    result = query_2ea_text_data(message, message, 'card.sql')
    response = response_card_data(result)
    response = json.dumps(response, ensure_ascii=False).encode('utf8')
    return Response(response, content_type='application/json; charset=utf-8', status=200)                

if __name__ == '__main__':
    app.run()