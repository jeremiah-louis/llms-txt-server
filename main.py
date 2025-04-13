from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from markitdown import MarkItDown

app = FastAPI()
md = MarkItDown(enable_plugins=False)

class URLInput(BaseModel):
    url: str

@app.post("/generate-md")
async def generate_markdown(input: URLInput):
    try:
        result = md.convert(input.url)
        return {"markdown": result.text_content}
    except Exception as e:
        return {"error": str(e)}

@app.get("/health")
async def health_check():
    return {"status": "ok"}
