# Project config #

## Install and activate virtualenv ##

```
#!bash
virtualenv -p /usr/bin/python3 .env
. .env/bin/activate
```

## Create file with local settings(see settings_example.py) ##
```
#!bash
touch ./hubs/settings_local.py
```

## Install requirements ##

```
#!bash
pip install -r requirements_base.txt
pip install -r requirements_local.txt
```

## Create database ##

```
#!bash
./manage.py migrate
```

## Create superuser ##

```
#!bash
./manage.py createsuperuser
```


SKIP celery


## Start Celery ##
```
#!bash
./manage.py celery worker -E -B -ldebug
```

## Start local server ##

```
#!bash
./manage.py runserver
```

After this site will be available on http://127.0.0.1:8000


SKIP rosetta


## Translation - create translation files in LOCALE_PATHS ##
```
#!bash
./manage.py makemessages -l ru
./manage.py makemessages -l ua
```
After go to rossetta-app and fill translation for each language
http://127.0.0.1:8000/rosetta/
Then apply changes and restart server
```
#!bash
./manage.py compilemessages
```


