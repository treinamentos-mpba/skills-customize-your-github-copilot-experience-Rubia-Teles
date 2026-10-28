import uvicorn
from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel

app = FastAPI(title="Reading List API")


class BookInput(BaseModel):
    title: str
    author: str


class Book(BookInput):
    id: int


books = [
    Book(id=1, title="The Hobbit", author="J. R. R. Tolkien"),
    Book(id=2, title="Frankenstein", author="Mary Shelley"),
]
next_book_id = 3


@app.get("/books", response_model=list[Book])
def list_books():
    # TODO: Return the current books.
    pass


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    # TODO: Find and return the book, or raise HTTPException with status 404.
    pass


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book_data: BookInput):
    # TODO: Create a book with next_book_id, add it to books, and return it.
    pass


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, book_data: BookInput):
    # TODO: Replace the book's title and author, or raise HTTPException with status 404.
    pass


@app.delete(
    "/books/{book_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    response_class=Response,
)
def delete_book(book_id: int):
    # TODO: Remove the book, or raise HTTPException with status 404.
    pass


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)