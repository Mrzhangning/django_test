from django.db import models
# data	status	style	city	type	group	introduce	detail
# Create your models here.
from mongoengine import  *

from mongoengine import connect
connect('excel',host='127.0.0.1',port=27017)

class itemInfo(Document):
    data = StringField()
    status = StringField()
    style = StringField()
    city = StringField()
    type = StringField()
    group = StringField()
    introduce = StringField()
    detail = StringField()

    meta = {
        'collection':'shuzhi'
    }

#for i in ArtiInfo.objects:
#  print(i .data,i.status,i.detail)