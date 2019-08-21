# FutureGov careers

A plain wagtail site.

## Running it locally

Make sure `python3`, `pip` and `pipenv` are installed

1. Clone the repo and `cd` into it
2. Activate the virtual environment with `pipenv shell` (or `python -m pipenv shell` if pipenv isn't in your PATH)

3. If running for the first time, run `pip install -r requirements.txt`, `python manage.py migrate` and `python manage.py createsuperuser`

4. Run it with `python manage.py runserver`p