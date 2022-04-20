import uuid
from django.db import models


class Students(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=20)


class Users(models.Model):
	name = models.CharField(max_length=20)
	email = models.EmailField()
