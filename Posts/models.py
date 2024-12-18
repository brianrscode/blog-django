from django.db import models
import uuid
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    title = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200, null=True, blank=True)
    description = RichTextUploadingField(null=True, blank=True)
    imagen_portada = models.ImageField(null=True, blank=True, default="default.jpg")
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title