from query import query_skill_data
from response import response_skill_data
from fastapi import FastAPI
import uvicorn

app = FastAPI()

# make endpoint
@app.get('/')
def index():
    return {'message': 'Hello World'}

@app.get('/skill')
def get_skill_data(message: str):
    result = query_skill_data(message)
    response = response_skill_data(result)
    return {'message': response}

if __name__ == '__main__':
    uvicorn.run(app, port=8000)
                
