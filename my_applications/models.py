from django.db import models

# Create your models here.
# after create model and admin you open new terminal and give python manage.py makemigrations my_applications it gives migration folder 
#then open new terminal and give python manage.py migrate it runs your models into query itvisible in sqlite
# in sqlite3 open database and choose my_applications_datas it shows your table columns

class Datas(models.Model):
    Name=models.CharField(max_length=20,default="")
    Age=models.IntegerField(default="")
    Address=models.CharField(max_length=20,default="")
    Contact=models.IntegerField(default="")
    Mail=models.CharField(max_length=50,default="")
