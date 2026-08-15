.PHONY: run lint makemigrations migrate

run:
	uv run python manage.py runserver

lint:
	uv run ruff check .

makemigrations:
	uv run python manage.py makemigrations

migrate:
	uv run python manage.py migrate