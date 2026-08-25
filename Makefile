.PHONY: run lint makemigrations migrate

run:
	uv run python manage.py runserver

lint:
	uv run ruff check

lint-fix:
	uv run ruff check --fix

makemigrations:
	uv run python manage.py makemigrations

migrate:
	uv run python manage.py migrate

test:
	uv run pytest

test-vv:
	uv run pytest -vv

test-cov:
	uv run pytest --cov=main --cov-report=term-missing