**RestingBlog** is a test project to Create, Retrive, Update, Delete and Search Blogs:

* API endpoints available for almost every module.
* Fast, easy and high performance application with django.
* Highly customizeable with as few lines of code as possible for application developers.

===========================
Features
===========================
----------------------------------------
* Functionality as a django application
----------------------------------------
  - User signup/login feature. Loose coupled app, that can be taken out easily and use anywhere else.
  - CRUD Operation for blogs along with other features.
  - Search feature to search ppt with title.
---------------
* API endpoints
---------------
  - https://elegant-livre-77487.herokuapp.com/api/v1/users/ (To check the details of all available users)
  - https://elegant-livre-77487.herokuapp.com/api/v1/user/(?P<term>[-\w]+)/ (search user with name/email/username containing the term searched)
  - https://elegant-livre-77487.herokuapp.com/api/v1/blogs/ (To get all Blogs + Create, Retrive and Update Done here)
  - https://elegant-livre-77487.herokuapp.com/api/v1/blog/delete/<id>/ (To  delete bload with id)
  - https://elegant-livre-77487.herokuapp.com/api/v1/blog/(?P<pk>[-\w]+)/ (to get blog with the pk provided)
  - https://elegant-livre-77487.herokuapp.com/api/v1/search/blog/?term=<any term that you want to search here> (gives a result list containning all blogs having a part of the searched term.)

===========================
Documentation
===========================

===========================
Demo
===========================

https://elegant-livre-77487.herokuapp.com

===========================
Technologies used
===========================
dj-database-url==0.4.0
gunicorn==19.4.5
psycopg2==2.6.1
whitenoise==2.0.6
Django==1.9.7
django-oauth-toolkit==0.10.0
django-rest-swagger==0.3.6
djangorestframework==3.3.3
ipython==4.2.0
django-ckeditor==5.0.3
python-slugify==1.2.0
