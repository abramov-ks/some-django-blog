# Getting started

## Requirements

- Python 3.x

## Run locally

From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open:

- Feed: `http://127.0.0.1:8000/`
- Admin: `http://127.0.0.1:8000/admin/`

## Create a post

1. Log into `/admin/`
2. Go to **Posts**
3. Click **Add Post**
4. Fill in title/content (slug auto-fills), keep **published** checked

