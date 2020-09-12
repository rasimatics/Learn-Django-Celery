from django.shortcuts import HttpResponse
from .tasks import sleepy

# Create your views here.

def index(request):
    sleepy.delay(3)
    return HttpResponse("<h1>Task is Done!")

