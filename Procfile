web: gunicorn portfolio_web.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
heroku ps:scale web=1
manage.py migrate