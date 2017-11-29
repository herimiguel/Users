from __future__ import unicode_literals
from django.db.models import Count
from django.contrib import messages
from apps.my_app.models import *


def create_users( first_name, last_name, email_address, age):
    user=User.objects.create(first_name = last_name, last_name=last_name, email_address=email_address, age=age)


# def valid_info():
#     users=User.objects.all()
#     for user in users:
#         print user.id, user.first_name, user.last_name, user.email_address, user.age



def all_info():
    users=User.objects.all().order_by('first_name')
    for user in users:
        print user.id, user.first_name, user.last_name, user.email_address, user.age

def get_user():
    users = User.objects.first() 
    print users.first_name

def update_info(user_id, last_name):
    user=User.objects.get(id=user_id)
    user.last_name=last_name
    user.save()
    print user.last_name

def delete_id(user_id):
    user=User.objects.get(id=user_id)
    user.delete()

