# FastAPI 진입점
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def root():
    return {'message': 'TradeMatch.AI 백엔드 동작 중'}
