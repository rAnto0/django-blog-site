MANAGE = python mydjangoproject/manage.py

.PHONY: install-dev run migrate makemigrations shell test check-django lint format format-check check load-fixtures reset-db

install-dev:
	uv sync --group dev

run:
	uv run $(MANAGE) runserver

migrate:
	uv run $(MANAGE) migrate

makemigrations:
	uv run $(MANAGE) makemigrations

shell:
	uv run $(MANAGE) shell

test:
	uv run $(MANAGE) test main_app users

check-django:
	uv run $(MANAGE) check

lint:
	uv run --group dev ruff check mydjangoproject/mydjangoproject

format:
	uv run --group dev ruff format mydjangoproject/mydjangoproject

format-check:
	uv run --group dev ruff format --check mydjangoproject/mydjangoproject

load-fixtures:
	uv run $(MANAGE) loaddata initial_data.json
	@uv run $(MANAGE) shell -c "from django.contrib.auth import get_user_model; from main_app.models import Category, TagPost, Posts; User = get_user_model(); print(f'Loaded: users={User.objects.count()}, categories={Category.objects.count()}, tags={TagPost.objects.count()}, posts={Posts.objects.count()}')"
	@printf "Login users: admin/admin12345, editor/editor12345\n"

reset-db:
	uv run $(MANAGE) flush --no-input

check: lint format-check check-django test
