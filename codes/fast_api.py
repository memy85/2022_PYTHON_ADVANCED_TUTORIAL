from typing import Optional 
import uvicorn
from fastapi import FastAPI
import asyncio 
from pathlib import Path


app = FastAPI()

@app.get('/')
async def root():
    return {"message":'Hello World'}

@app.get('/weights')
def return_txts():
    text = Path('/home/wonseok/2022_PYTHON_ADVANCED_TUTORIAL/data/my_text.txt')
    with open(text, 'r') as f :
        my_text = f.read()
    return {"this is my text":f"{my_text}"}

@app.get('/weights/{any_string}')
async def print_string(any_string: str):
          text = Path('/home/wonseok/2022_PYTHON_ADVANCED_TUTORIAL/data/my_text.txt')
          with open(text, 'r') as f :
              my_text = f.read()
          return {"this is my text":f"{my_text + any_string}"}    # 이렇게하면 request를 input할 수 있다. 


    


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)