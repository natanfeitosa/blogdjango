from taggit.managers import TaggableManager

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from django.contrib.auth.models import User
from django.db import models

class Article(models.Model):
    
    Thumbnail = models.ImageField(upload_to='thumb/')
    Title = models.CharField(max_length=255, blank=False, help_text='Nome do post')
    Created_at = models.DateField(auto_now_add=True)
    Summary = RichTextField(blank=False)
    Content = RichTextUploadingField(blank=False)
    Tag = TaggableManager()
    Author = models.ForeignKey(User, on_delete=models.PROTECT, blank=False)

    class Meta:
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.Title
