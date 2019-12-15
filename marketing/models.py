from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User

class imagePromo(models.Model):
    linked = (
        ('/product/detail/grand-amelia', 'amelia'),
        ('/product/detail/garden-asri', 'garden asri'),
        ('/product/detail/garden-cluster-kepanjen', 'Garden Cluster'),
        ('/product/detail/puri-taman-agung', 'PTA')
        )
    Nama_promo = models.CharField(max_length=120,blank=False)
    Image_promo = models.ImageField(upload_to="promosi", 
    null=True,
    blank=True,
    editable=True,
    help_text="Ukuran image 1920x960",
    verbose_name="Promo Picture")
    link = models.CharField(max_length=500, choices=linked, blank=True, null=True)
    published   = models.DateTimeField(auto_now_add=True)
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.Nama_promo
class promosi(models.Model):
    nama_promosi = models.CharField(max_length=250)
    Pilih_Promosi = models.ManyToManyField(imagePromo)
    updated = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "{}".format(self.updated)


