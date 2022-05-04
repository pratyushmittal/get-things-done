#!/bin/bash

# On git push, this script will run automatically on server

set -e  # exit if anything fails

echo "Installing requirements"
pip3.9 install --upgrade pip --user
pip3.9 install -r requirements/requirements.txt --user

echo "Collecting Static files"
python3.9 manage.py collectstatic --noinput --settings=get_things_done.settings.production

echo "Running migrations"
python3.9 manage.py migrate --settings=get_things_done.settings.production

echo "Restarting uwsgi"
touch get_things_done/wsgi.py

echo "Updating crons"
crontab < deploy/crons.crontab

echo "Successfully Deployed. Woohoo!"
