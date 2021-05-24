import uuid
from django.db import models


class Cat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    breeed = models.CharField(max_length=100, unique=True)
    location_of_origin = models.CharField(max_length=100)
    coat_length = models.CharField(max_length=100)
    body_type = models.CharField(max_length=100)
    pattern = models.CharField(max_length=100)

    def __str__(self):
        return self.breeed
