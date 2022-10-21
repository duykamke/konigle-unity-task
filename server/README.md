# UNITY WEB APPLICATION - Django + REST Framework

## Environment
- Linux - WSL2 on Windows
- Python 3.8.5 - Using virtual environment

## Libraries used
- Celery - 5.2.7 - For periodic tasks
- Django - 4.1.2 - Python web application framework
- DjLint - 1.19.1 - For Django HTML linting
- Django REST Framework - 3.14.0 - REST compatible framework
- Django CORS Headers - 3.13.0 - To configure CORS
- Redis - 4.3.4 - As broker and backend database to be used with celery

## Usage (development only)
1. Install requirements with `pip install -r requirements.txt`.
2. Run development server with `python manage.py runserver`.
3. For periodic task:
    - Install redis with `sudo apt-get update` and `sudo apt-get install redis`.
    - Run redis server with `redis-server` in a seperate terminal.
    - Run `celery -A server worker -B -l info`.