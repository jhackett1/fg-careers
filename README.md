# FutureGov careers

A plain wagtail site.

## Running it locally

Make sure `python3`, `pip` and `pipenv` are installed

1. Clone the repo and `cd` into it
2. Activate the virtual environment with `pipenv shell` (or `python -m pipenv shell` if pipenv isn't in your PATH)

3. If running for the first time, run `pip install -r requirements.txt`, `python manage.py migrate` and `python manage.py createsuperuser`

4. Run it with `python manage.py runserver`

5. If you want to compile sass and JS, run `npm i` and then `npm run dev` in a separate terminal.


## Sass

Making sass work in django was tougher than expected and there are no good video tutorials.

Here are the steps to make it work in **development**:

1. Use [this repo](https://github.com/jrief/django-sass-processor)
2. Run `pip install libsass django-compressor django-sass-processor`
3. On Windows, you may need to install the Visual Studio build tools [from here](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=16) for step 2 to succeed
4. Add `sass_processor` to the list of installed Django apps in settings
5. Add `sass_processor.finders.CssFinder` to the `STATICFILES_FINDERS` array in settings
6. Add `{% load sass_tags %}` to the **top** of any templates using sass
7. Reference sass files like this: `<link href="{% sass_src 'style.scss' %}" rel="stylesheet" type="text/css" />`