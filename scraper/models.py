import uuid
from django.db import models


# Create your models here.
class FormDetails(models.Model):
    formdetails = models.JSONField()


