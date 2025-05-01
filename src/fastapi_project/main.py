from fastapi import FastAPI, HTTPException
from typing import List, Union, Any
from pydantic import BaseModel
from fastapi.openapi.utils import get_openapi
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],  # Allow requests from this origin only (for development)
    # allow_origins=["*"],  # Uncomment this line to allow all origins (not recommended for production)
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
    return {"message": "Welcome to Library!"}

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

# Customize the OpenAPI schema to add a "Servers" dropdown
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="FastAPI",
        version="0.1.0",
        description="My FastAPI app with a Development Server",
        routes=app.routes,
    )
    # Add the "servers" list with a Development Server
    openapi_schema["servers"] = [
        {
            "url": "http://0.0.0.0:8000",  # The server URL (matches your Docker setup)
            "description": "Development Server"  # The name shown in the dropdown
        }
    ]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

# Assign the custom_openapi function to override the openapi method
app.openapi_schema = custom_openapi()