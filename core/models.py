from django.db import models
from django.urls import reverse
from uuid import uuid4
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(models.Model):
    title = models.CharField(max_length=200)

    body = models.TextField()

    def __str__(self):
        return self.title


