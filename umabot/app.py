import json
from query import query_skill_data
from response import response_skill_data
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

    result = query_skill_data(message)
    response = response_skill_data(result)
    response = json.dumps(response, ensure_ascii=False).encode('utf8')
    return Response(response, content_type='application/json; charset=utf-8', status=200)
                
if __name__ == '__main__':
    app.run()