import importlib.util
from pathlib import Path

import pytest
from fastapi.testclient import TestClient


api_path = (
    Path(__file__).resolve().parents[1]
    / "fastapi-rest-api"
    / "starter-code.py"
)
api_spec = importlib.util.spec_from_file_location("student_api", api_path)
if api_spec is None or api_spec.loader is None:
    raise ImportError(f"Could not load the FastAPI application from {api_path}")

api = importlib.util.module_from_spec(api_spec)
api_spec.loader.exec_module(api)
client = TestClient(api.app)


@pytest.fixture(autouse=True)
def reset_books():
    api.books[:] = [
        api.Book(id=1, title="The Hobbit", author="J. R. R. Tolkien"),
        api.Book(id=2, title="Frankenstein", author="Mary Shelley"),
    ]
    api.next_book_id = 3


def test_list_books_returns_expected_books():
    pytest.fail("Add assertions for GET /books")


def test_get_existing_book_returns_book():
    pytest.fail("Add assertions for GET /books/{book_id}")


def test_get_unknown_book_returns_404():
    pytest.fail("Add assertions for a missing book ID")


def test_create_book_returns_created_book():
    pytest.fail("Add assertions for POST /books")


def test_update_book_changes_book_details():
    pytest.fail("Add assertions for PUT /books/{book_id}")


def test_delete_book_removes_book():
    pytest.fail("Add assertions for DELETE /books/{book_id}")


def test_update_and_delete_unknown_book_return_404():
    pytest.fail("Add assertions for missing book IDs on PUT and DELETE")