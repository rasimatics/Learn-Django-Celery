from django.shortcuts import render,redirect
from .tasks import *
from .models import SharedExampleModel,PeriodicExampleModel


def index(request):
    instances1 = SharedExampleModel.objects.all() # get all instances from model
    instances2 = PeriodicExampleModel.objects.all()  # get all instances from model
    return render(request,"index.html",{'instances1':instances1,"instances2":instances2}) # render context

# Instance create view
def addInstance(request):
    add_instance_shared.delay() # send task to celery
    return redirect('/') # redirect to index view

