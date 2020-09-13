from django.contrib import admin
from .models import SharedExampleModel,PeriodicExampleModel

admin.site.register(SharedExampleModel)
admin.site.register(PeriodicExampleModel)

# Register your models here.
