# copy the code directory to remote
# the run following commands
echo "run on local\n$ scp -r deploy get_things_done:"
cd deploy/uberspace

set -e

# create folders
mkdir ~/repos
git init --bare ~/repos/get_things_done.git
cp ../post-receive ~/repos/get_things_done.git/hooks/post-receive
chmod +x ~/repos/get_things_done.git/hooks/post-receive
mkdir ~/webapps

# https://lab.uberspace.de/guide_django.html
# install uwsgi
pip3.9 install uwsgi --user
cp uwsgi.ini ~/etc/services.d/uwsgi.ini
mkdir -p ~/uwsgi/apps-enabled
touch ~/uwsgi/err.log
touch ~/uwsgi/out.log

supervisorctl reread
supervisorctl update
supervisorctl status

# configure web server
uberspace web domain add www.get-things-done.com
uberspace web backend set www.get-things-done.com --http --port 8000

# create deamon
mkdir -p ~/uwsgi/apps-enabled/
cp django-app.ini ~/uwsgi/apps-enabled/

# configure static servers
uberspace web backend set www.get-things-done.com/static --apache
uberspace web backend set www.get-things-done.com/media --apache

# add nginx headers
uberspace web header set www.get-things-done.com/static/ expires 7d
uberspace web header set www.get-things-done.com/favicon.ico root /var/www/virtual/getdone/html/static/favicons
uberspace web header set www.get-things-done.com/favicon.ico expires 7d

uberspace web header set www.get-things-done.com/static gzip on
uberspace web header set www.get-things-done.com/static gzip_comp_level 6
uberspace web header set www.get-things-done.com/static gzip_types text/plain text/css text/xml application/json application/javascript application/xml+rss application/atom+xml image/svg+xml
uberspace web header set www.get-things-done.com/static gzip_types "text/plain text/css text/xml application/json application/javascript application/xml+rss application/atom+xml image/svg+xml"


# import content
python3.9 manage.py migrate --settings=get_things_done.settings.production
python3.9 manage.py createsuperuser --settings=get_things_done.settings.production

# instructions to setup git push
echo "Remote setup done"
echo "Run these on local"
echo "git remote add live getdone:/repos/get_things_done.git"
echo "git push live"
