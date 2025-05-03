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

# Dummy empty data storage in the form of dictionary
books: list[Book] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to Library API."}

@app.get("/books", response_model=List[Book])
def get_books():
    return books

@app.get("/books_1", response_model=Union[List[Book], dict])
def get_books_1():
    if not books:
        return {"message": "No books available"}
    return books

@app.post("/books", response_model=Book)
def add_book(book: Book):
    books.append(book)
    return book

@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for book in books:
        if book.id == book_id:
            books.remove(book)
            return {"message": "Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")
