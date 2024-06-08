from fastapi import FastAPI
import pandas as pd
from pydantic import BaseModel

app = FastAPI()

class languageModel(BaseModel):
    get_language:str


df = pd.read_csv("dataset.csv")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get('/languages')
async def languages():
    lang_response = list(df['LANGUAGE'].unique())
    return lang_response

@app.post("/custom-language/")
async def get_custom_language(language: languageModel):
    request_language = language.get_language
    my_json  = df[df['LANGUAGE'] == request_language].to_json(orient='records')
    return my_json