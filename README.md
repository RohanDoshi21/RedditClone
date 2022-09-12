Heroku Django Deployment
1. Create Procfile, requirements.txt, runtime.txt
2. Add gunicorn to installed apps
3. Change Database to heroku Postgres
4. Modify settings.py to support static file collection on heroku
5. git push heroku HEAD:master