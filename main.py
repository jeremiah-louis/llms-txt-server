from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from markitdown import MarkItDown
from pymongo import MongoClient
from decouple import config

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Your Next.js frontend domain
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

md = MarkItDown(enable_plugins=False)

# Initialize MongoDB client
client = MongoClient(config("MONGO_CLIENT_URI"))
db = client[config("MONGO_DB_NAME")]
collection = db[config("MONGO_COLLECTION_NAME")]

class URLInput(BaseModel):
    url: str

@app.post("/generate-md")
async def generate_markdown(input: URLInput):
    try:
        result = md.convert(input.url)
        markdown_content = result.text_content

        # Record the URL and markdown in MongoDB
        collection.insert_one({
            "url": input.url,
            "markdown": markdown_content
        })

        return {"markdown": markdown_content}
    except Exception as e:
        return {"error": str(e)}

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.get("/")
async def main_index():
    return {"status": "ok"}
