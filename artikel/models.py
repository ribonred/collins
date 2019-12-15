from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from tinymce import HTMLField
from django.db import migrations
from django.core.signals import request_finished
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

class perijinan(models.Model):
    Title_artikel = models.CharField(max_length=255, blank=True)
    Materi        = HTMLField('content')
    publish       = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Title_artikel

class pengembangan (models.Model):
    Category_select = (
        ('pengembangan', 'pengembangan'),
    ('pembangunan', 'pembangunan'),
    ('news', 'news'),
    )
    judul=models.CharField(max_length=255)
    isi2=RichTextUploadingField()
    thumbnail=models.ImageField(upload_to='pengembangan pic',blank=True, null=True)
    kategori=models.CharField(max_length=250, choices=Category_select)
    published=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    slug=models.SlugField(blank=True, editable=True, max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def save(self):
        self.slug = slugify(self.judul)
        super().save()
    def get_absolute_url(self):
        url_slug={'slug':self.slug}
        return reverse("pengembangan:detail", kwargs=url_slug)
    
    

    def __str__(self):
        return "{}. {}".format(self.judul, self.published)

