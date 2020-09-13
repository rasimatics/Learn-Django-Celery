from django.db import models


class SharedExampleModel(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

class PeriodicExampleModel(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name
