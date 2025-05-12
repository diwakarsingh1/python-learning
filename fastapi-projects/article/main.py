from fastapi import FastAPI
import schemas
import uvicorn
from typing import Optional


app = FastAPI()



@app.post('/create_article')
def create_articel(request: schemas.Article):
    return {f'Your article with title {request.title} is posted with body {request.body}'}