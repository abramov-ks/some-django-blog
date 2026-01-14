# AGENTS.md

This repository may be worked on by **AI coding agents** (including Cursor agents). This document defines what an agent is expected to do, how it should operate in this codebase, and the conventions it must follow.

## What an “agent” means here

An **agent** is an automated contributor that can:

- Read and modify source code in this repo
- Run local commands (tests, linters, formatting, Django management commands)
- Propose and apply patches in small, reviewable increments

Agents should behave like a careful teammate: prioritize correctness, security, readability, and minimal diff size.

## Project overview (for agents)

This is a small **Django** project with:

- A Django project in `config/`
- A Django app in `blog/`
- Templates in `templates/`
- Static assets in `static/`

## Rules of engagement

- **Prefer small, atomic changes**: make the smallest change that satisfies the request.
- **Be explicit**: when behavior changes, update docs/templates/tests accordingly.
- **Avoid unrelated refactors** unless explicitly requested.
- **Do not commit secrets**: never add API keys, credentials, or tokens to the repo.
- **Treat user input as untrusted**: use Django’s built-in protections and escaping.
- **Keep the app runnable**: changes should not break `python manage.py runserver` or migrations.

## Development commands

From the repository root:

- **Install deps**:

```bash
python -m pip install -r requirements.txt
```

- **Run the server**:

```bash
python manage.py runserver
```

- **Run migrations**:

```bash
python manage.py makemigrations
python manage.py migrate
```

- **Run tests** (if/when added):

```bash
python manage.py test
```

## Django conventions in this repo

- **URLs**:
  - Project routing: `config/urls.py`
  - App routing: `blog/urls.py`
- **Templates**:
  - Base layout: `templates/base.html`
  - Blog templates: `templates/blog/`
- **Static files**:
  - CSS: `static/app.css`
- **Models & migrations**:
  - Models: `blog/models.py`
  - Migrations: `blog/migrations/`

## Quality bar checklist (before declaring “done”)

- **Behavior matches the request** and edge cases are considered
- **No obvious security issues** (XSS, unsafe file ops, unsafe deserialization)
- **Docs updated** if usage/behavior changes
- **Reasonable naming and comments** where clarity is needed

## If you’re an agent reading this

When a request is ambiguous, ask one targeted question — otherwise make a sensible default choice and document it in the change.

