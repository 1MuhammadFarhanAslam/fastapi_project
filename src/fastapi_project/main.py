# app/main.py
from fastapi import FastAPI, HTTPException
from typing import List, Union, Any
from pydantic import BaseModel

app = FastAPI()

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

@app.get("/books", response_model=List[Book]) # Example of using List for response model if books are available
def get_books():
    return books

@app.get("/books_1", response_model=Union[List[Book], dict])   # Example of using Union for response model when no books are available
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
