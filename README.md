# FutureGov careers

A plain wagtail site.

## Running it locally

Make sure `python3`, `pip` and `pipenv` are installed

1. Clone the repo and `cd` into it
2. Activate the virtual environment with `pipenv shell` (or `python -m pipenv shell` if pipenv isn't in your PATH)

3. If running for the first time, run `pipenv install`, `python manage.py migrate` and `python manage.py createsuperuser`

4. Run it with `python manage.py runserver`

5. If you want to compile sass and JS, run `npm i` and then `npm run dev` in a separate terminal.

## pipenv

This is a pipenv project. That means that rather than running `pip install`, you should run `pipenv install`.

Rather than a `requirements.txt` file, you have a `Pipfile` and a `Pipfile.lock`.

## psycopg2

If you run into trouble installing psycopg2 on OSX:

`sudo installer -pkg /Library/Developer/CommandLineTools/Packages/macOS_SDK_headers_for_macOS_10.14.pkg -target /`

[StackOverflow explanation](https://stackoverflow.com/questions/34304833/failed-building-wheel-for-psycopg2-macosx-using-virtualenv-and-pip)
