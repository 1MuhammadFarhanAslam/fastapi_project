from fastapi import FastAPI, HTTPException
from typing import List, Union, Any
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="FastAPI Development Server",
        version="0.1.0",
        description="My FastAPI app with a Development Server",
            servers=[
        {
            "url": "http://localhost:8000", # ADD NGROK URL Here Before Creating GPT Action
            "description": "Development Server"
        }
        ])

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    # allow_origins=["http://localhost:8000"],  # Allow requests from this origin only (for development)
    allow_origins=["*"],  # Uncomment this line to allow all origins (not recommended for production)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Book model
class Book(BaseModel):
    """
    Book model to represent a book in the library.
    """
    id: int 
    title: str
    author: str
    year: int

@app.get("/")
def read_root():
    return {"message": "Welcome to Library API. Today is a good day to read a book!"}
