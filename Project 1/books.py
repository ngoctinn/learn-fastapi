from fastapi import Body, FastAPI

app = FastAPI()

BOOKS = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"id": 3, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"id": 4, "title": "Pride and Prejudice", "author": "Jane Austen"},
]

@app.get("/books")
async def get_books():
    return BOOKS