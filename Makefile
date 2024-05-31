make install:
	poetry install --no-root

start:
	poetry run uvicorn main:app --reload