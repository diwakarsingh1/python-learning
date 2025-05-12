from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get('/')

def index():
    return {'data':{'name': 'diwakar'}}

@app.get('/about')
def about():
    return {'data': 'diwakar'}

#dynamic routing

@app.get('/article')
def article(limit=50, published: bool = False):
    if published:
        return {'article': f'{limit} published article is here from database'}
    else:
        return {'article': f'{limit} article is here from database'}

@app.get('/article/{article_no}')
def get_article(article_no: int):
    return {'article': article_no}

@app.get('/article/{article_no}/diwakar')
def article_comment(article_no: int):
    return {'article': {'1' : article_no }}


class Article(BaseModel):
    title: str
    body: str
    want_to_publish: Optional[bool]

@app.post('/create_article')
def create_article(article: Article):
    # return submit
    return {f'Your article {article.title} is posted'}



if __name__ == "_main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)