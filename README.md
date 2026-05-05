# Django Blog Site

Учебный Django-проект блога с локальным запуском.

## Что реализовано

- Django 5, кастомная модель пользователя, email-аутентификация
- SQLite для локальной разработки
- uv + `pyproject.toml` для зависимостей
- Makefile для типовых команд
- Публикация постов, категории, теги, страница поста, профиль пользователя
- Готовая демо-фикстура для быстрого просмотра проекта

## Быстрый старт

### 1) Установка зависимостей

```bash
make install-dev
```

### 2) Миграции, загрузка фикстур и запуск

```bash
make migrate
make load-fixtures
make run
```

`http://127.0.0.1:8000`

## Основные команды

- `make install-dev` - установить зависимости через uv
- `make run` - локальный запуск Django
- `make migrate` - применить миграции
- `make reset-db` - очистить все данные во всех таблицах
- `make load-fixtures` - загрузить демо-данные из `initial_data.json`
- `make test` - запустить тесты
- `make lint` - запустить ruff check
- `make format` - запустить ruff format
- `make check` - lint + format-check + test

## Демо-пользователи

После `make load-fixtures` можно войти под готовыми аккаунтами:

- `admin` / `admin12345`
- `editor` / `editor12345`

## Переменные окружения (опционально)

Моджно создать `.env` в корне проекта при необходимости.

- `DEBUG`
- `SECRET_KEY`
- `ALLOWED_HOSTS`
- `EMAIL_HOST_USER`
- `EMAIL_HOST_PASSWORD`
