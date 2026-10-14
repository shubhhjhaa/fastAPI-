# fAPI

A small FastAPI application for retrieving user records by ID.

## Project structure

- `todo.py` - main FastAPI app

## Features

- `GET /users/{user_id}` returns user data for the user with ID 1
- Returns `404` with a message when the requested user does not exist

## Requirements

- Python 3.10+
- FastAPI
- Uvicorn

## Setup

Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
pip install fastapi uvicorn
```

## Run the app

```bash
uvicorn todo:app --reload
```

Then open the API docs in your browser:

- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/redoc

## Example request

```bash
curl http://127.0.0.1:8000/users/1
```

## Notes

This project is a minimal example and can be expanded with additional routes, validation, and database integration as needed.
