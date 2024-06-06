PORT ?= 8080


make install:
	poetry install --no-root

start:
	poetry run uvicorn main:app --host 0.0.0.0 --port $(PORT) --reload