## Step-by-Step Guide: Install Poetry on Windows

### Step 1: Open PowerShell as Administrator

- Press `Win` key
- Type `powershell`
- Right-click on **Windows PowerShell** ➜ **Run as Administrator**

### Step 2: Run the Official Install Command

Copy-paste this command in PowerShell:

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

Make sure `python` command works. If not, use `python3`.


### Step 3: Close and Reopen Terminal

After successful installation, **close PowerShell**, then open a **new one** (or use CMD or Git Bash).

Now check if Poetry is installed:

```bash
poetry --version
```

Output should look like: `Poetry version 1.7.x` (or latest)

### Step 4: Add Poetry to PATH (if not auto-added)

If you get `'poetry' is not recognized...`, add it manually:

1. Find path:  
   Default is usually:
   ```
   C:\Users\YourName\AppData\Roaming\Python\Scripts
   ```

2. Add this to your system’s **Environment Variables** ➜ `Path`

3. Reopen terminal ➜ run `poetry --version`

---
## How to initialize poetry project/package
- `poety new project_name`
- `cd project_name`
---
## How to activate poetry env
Looking for poetry shell? It was moved to a plugin: `poetry-plugin-shell`
The poetry env activate command prints the activate command of the virtual environment to the console. You can run the output command manually or feed it to the eval command of your shell to activate the environment. 


#### Recommended Way — Use `env activate`

### Step-by-step:

1. First, **create/init** your project (if not already done):
```bash
poetry init
```

2. Activate the virtual environment:
```bash
poetry env list --full-path
```

This will show something like:
```
C:\Users\username\.cache\pypoetry\virtualenvs\fastapi_project-abc123-py3.10
```

3. Now **activate it manually** using:

```powershell
& "C:\Users\username\.cache\pypoetry\virtualenvs\fastapi_project-abc123-py3.10\Scripts\Activate.ps1"
```

Your path will be **different** — copy-paste from the output of `poetry env list --full-path`

1. Then install FastAPI & dependencies:
```bash
poetry add fastapi uvicorn[standard]
```

#### Option 2: Install Old `shell` Plugin (if you miss `poetry shell`)

```bash
poetry self add poetry-plugin-shell
```

Now you can run:
```bash
poetry shell
```
---

## How to create `main.py` and run fastapi server 

Inside your project folder, make a file named:

```
src/main.py
```

Then put this code in it:

```python
# src/main.py
from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

app = FastAPI()

# Dummy data storage
books = []

# Book model
class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int

@app.get("/")
def read_root():
    return {"message": "Welcome to Pind ki Library!"}

@app.get("/books", response_model=List[Book])
def get_books():
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
    return {"error": "Book not found"}

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for book in books:
        if book.id == book_id:
            books.remove(book)
            return {"message": "Book deleted"}
    return {"error": "Book not found"}
```

#### Step 2: Run the Server

In your terminal, run:

```bash
poetry run uvicorn app.main:app --reload
```

You’ll see something like:

```
Uvicorn running on http://127.0.0.1:8000
```

---

## Step 3: Test it in Browser!

Open these:

- **Docs**: http://127.0.0.1:8000/docs
- **Root**: http://127.0.0.1:8000

---

## What You’ve Built So Far:

| Method | URL                  | Description              |
|--------|----------------------|--------------------------|
| GET    | `/books`             | Show all books           |
| POST   | `/books`             | Add a new book           |
| GET    | `/books/{book_id}`   | Get a single book        |
| DELETE | `/books/{book_id}`   | Delete a book            |

---
## Add pytest to dependencies

- `poetry add --group dev pytest`

## How to run pytest
- `poetry run pytest`
- `poetry run pytest -v`
- `poetry run pytest -vv`
  
---
