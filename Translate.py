from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Translation(BaseModel):
    text1: str
    text2: str


# class TranslationResponse(BaseModel):
#     translated_text: str

@app.post('/translate/')
def translate_text(translated_text: Translation):
    # text = request['text']
    # if not text:
        # raise HTTPException(status_code=400, detail="Text is required")
    text1=translated_text.text1
    text2=translated_text.text2
    # فراخوانی مدل مترجم
    translated_tex = model_translate(text1) + model_translate(text2)
    
    return translated_tex

# تابع model_translate را با مدل واقعی خود جایگزین کنید
def model_translate(text):
    # اینجا مدل مترجم شما کار می‌کند
    # برای مثال، یک ترجمه ساده برگردانده می‌شود
    return text

