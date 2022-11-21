import uuid
from django.db import models


# Create your models here.
class BaseModel(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

class Customers(BaseModel):
    customer_name = models.TextField(max_length=100)
    customer_url = models.URLField()
