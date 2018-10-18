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


### Clustering Analysis


k-means

グラフ理論

確率分布

Gaussian Mixture

文章の指標化


 - [Tf-idf](https://ja.wikipedia.org/wiki/Tf-idf)
    - 文書中に含まれる単語の重要度を評価する手法の1つ
    
    tf-idfを利用して、文章の中に含まれる単語の重要度を上げる


