from django.db import models
import uuid
# Create your models here.

class metadata(models.Model):
    fileIdentifier = models.UUIDField(
         default = uuid.uuid4,
         editable = True)
    title = models.TextField(blank=False)
    xml = models.TextField(blank=False)

    def __str__(self):
         return f"{self.title} {self.fileIdentifier}"
