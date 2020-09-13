from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.task import periodic_task
from celery.schedules import crontab
from .models import SharedExampleModel,PeriodicExampleModel
import time,random

# add shared task: create 2 instaces of SharedExampleModel
@shared_task
def add_instance_shared():
    for i in range(2):
        instance = SharedExampleModel(name=str(random.randint(1000,10000)))
        instance.save()

# add periodic task: create an instance of PeriodicExampleModel
@shared_task
def add_instance_periodic():
    instance = PeriodicExampleModel(name=str(random.randint(1000,10000)))
    instance.save()

    