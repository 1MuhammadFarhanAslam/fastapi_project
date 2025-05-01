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

## Let's Containerize the FastAPI App

This project is a simple FastAPI app containerized with Docker for easy deployment and development.

## Requirements

- [Docker](https://www.docker.com/)
- (Optional) [Poetry](https://python-poetry.org/) if running locally without Docker



### Step 1: Check if Docker is Running
```bash
docker version
```

### Step 2: Build the Image for Development
```bash
docker build -f Dockerfile.dev -t fastapi-dev-image .
```

### Step 3: Check Available Images
```bash
docker images
```

### Step 4: Inspect the Image
```bash
docker inspect fastapi-dev-image
```

### Step 5: Run the Container in Dev Mode
```bash
docker run -d --name fastapi-dev-cont -p 8000:8000 fastapi-dev-image
```

Open in browser:
```
http://localhost:8000
http://localhost:8000/docs
```

### Step 6: View Container Logs
```bash
docker logs fastapi-dev-cont
```

### Step 7: Run Tests inside the Image (without starting container)
```bash
docker run -it --rm fastapi-dev-image /bin/bash -c "poetry run pytest"
```

---

### Step 8: List Running Containers
```bash
docker ps
```

---

### Step 9: List All Containers (including stopped ones)
```bash
docker ps -a
```

### Step 10: Interact with Running Container (Shell)
```bash
docker exec -it dev-cont1 /bin/bash
```

### Exit the Shell
```bash
exit
```

## If the container doesn't start correctly

Run this to debug interactively:
```bash
docker run -it fastapi-dev-image /bin/bash
```

---

## Delete Docker Images – Commands You Need

### 1. **List all Docker images**
```bash
docker images
```

### 2. Delete a specific image by name or ID
```bash
docker rmi IMAGE_ID
```

**Example:**
```bash
docker rmi fastapi-dev-image
```

If the image is used by a container (even stopped), you’ll get an error. To force delete:

```bash
docker rmi -f IMAGE_ID
```

### 3. **Delete ALL unused (dangling) images**
```bash
docker image prune
```

Or more aggressively:
```bash
docker image prune -a
```

This will:
- Remove all images **not used by any container**
- Ask for confirmation

To skip confirmation:
```bash
docker image prune -a -f
```

### 4. **Delete ALL images**
```bash
docker rmi -f $(docker images -q)
```

This will remove ALL images — use with caution!

---

## Debugging stopped containers

**Docker container is NOT running**

```
docker ps
# → No output = No running container
```

You ran:

```bash
docker run -d --name fastapi-dev-cont -p 8000:8000 fastapi-dev-image
```


Run this command to see **stopped containers**:

```bash
docker ps -a
```

Now, view the error that caused the crash:

```bash

docker logs fastapi-dev-cont
```

## Stop and remove old container

```bash
docker stop fastapi-dev-cont
docker rm fastapi-dev-cont
```

## Rebuild the image

```bash
docker build -f Dockerfile.dev -t fastapi-dev-image .
```

## Run container again

```bash
docker run -d --name fastapi-dev-cont -p 8000:8000 fastapi-dev-image
```

