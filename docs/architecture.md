# Architecture

## High-level

This project is a minimal Django blog using **SQLite** for storage and Django templates for rendering.

## Directory layout

- `config/`: Django project configuration (settings, root URLs, WSGI/ASGI)
- `blog/`: blog app (models, views, app URLs, admin)
- `templates/`: HTML templates (`templates/base.html` and `templates/blog/*`)
- `static/`: static assets (CSS in `static/app.css`)
- `db.sqlite3`: local SQLite database (generated/updated by migrations)

## Core concepts

- **Posts**: stored in `blog.models.Post`
- **Feed page**: `blog.views.post_list` renders `templates/blog/post_list.html`
- **Post detail**: `blog.views.post_detail` renders `templates/blog/post_detail.html`
- **Admin**: Django admin at `/admin/` for creating/editing posts

## URLs

- `/`: blog feed (post list)
- `/posts/<slug>/`: post detail
- `/admin/`: admin UI

