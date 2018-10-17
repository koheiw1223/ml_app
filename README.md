ml_app
===

## Django memo

##### create project

```
$ sudo docker-compose run ml_app django-admin.py startproject ml_app .
```

 - [check list](https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/)

##### start
 
```
$ docker-compose up
```

##### add superuser

```
$ docker exec -it  ml_app_ml_app_1 /bin/bash
$ python manage.py createsuperuser
```


##### create app

```
$ python manage.py startapp <app_name>
```