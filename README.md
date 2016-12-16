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


## Start Celery ##
```
#!bash
./manage.py celery worker -E -B -ldebug
```


