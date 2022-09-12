Heroku Django Deployment
1. Create Procfile, requirements.txt, runtime.txt
2. Add gunicorn to installed apps
3. heroku config:set DISABLE_COLLECTSTATIC=1
3. git push heroku HEAD:master
