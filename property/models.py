from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from tinymce import HTMLField
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from django.shortcuts import get_object_or_404

    
class Customer(models.Model):
    Pembayaran = (
        ('KPR', 'KPR'),
        ('Tunai Keras', 'Tunai Keras'),
        ('InHouse','InHouse')
    )
    user                            = models.ForeignKey(User, on_delete=models.CASCADE)
    nama                            = models.CharField(max_length=200)
    alamat                          = models.CharField(max_length=200)
    kirim_notifikasi                = models.BooleanField(default=False)
    Notlp                           = models.DecimalField(max_digits=12, decimal_places=0)
    No_id                           = models.DecimalField(max_digits=15, decimal_places=0)
    cara_bayar                      = models.CharField(choices=Pembayaran, max_length=250, null=True, blank=True)
    Jumlah_booking                  = models.DecimalField(decimal_places=0, max_digits=30, blank=True, null=True)
    Booking_Date                    = models.DateField(blank=True, null=True)
    data_ktp_suami                  = models.BooleanField(default=False)
    data_ktp_istri                  = models.BooleanField(default=False)
    data_kk                         = models.BooleanField(default=False)
    data_surat_nikah                = models.BooleanField(default=False)
    data_npwp                       = models.BooleanField(default=False)
    data_rek                        = models.BooleanField(default=False)
    data_slip_gaji                  = models.BooleanField(default=False)
    data_ket_kerja                  = models.BooleanField(default=False)
    pembaruan_data                  = models.BooleanField(default=False)
    persetujuan                     = models.BooleanField(default=False)
    tgl_persetujuan_prinsip         = models.DateField(blank=True, null=True)
    tgl_sp3k                        = models.DateField(blank=True, null=True)
    jumlah_sp3k                     = models.DecimalField(decimal_places=0, max_digits=30, blank=True, null=True)
    Bank                            = models.CharField(max_length=255, blank=True, null=True)
    tgl_realisasi                   = models.DateField(blank=True, null=True)
    image_realisasi                 = models.ImageField(upload_to='data user', blank=True, null=True)
    tgl_serah_terima                = models.DateField(blank=True, null=True)
    image_serah_terima              = models.ImageField(upload_to='data user', blank=True, null=True) 

    def __str__(self):
        return self.nama

class uangmuka(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='uang_muka')
    jumlah = models.DecimalField(decimal_places=0,max_digits=30, blank=True, null=True)
    keterangan = models.CharField(max_length=255)
    tgl_byr = models.DateField(blank=True, null=True)
class ProsesBangun(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='prosesbangun')
    keterangan = models.CharField(max_length=255)
    foto = models.ImageField(upload_to='data user', blank=True, null=True)
    tgl = models.DateField(blank=True, null=True)
class ameneties(models.Model):
    ameneties = models.CharField(max_length=250)

    def __str__(self):
        return self.ameneties

class kondisi(models.Model):
    name  = models.CharField(max_length=255)
    slug    = models.SlugField(blank=True, editable=True)
    def save(self):
        self.slug = slugify(self.name)
        super().save()
    def get_absolute_url(self):
        url_slug={'slug':self.slug}
        return reverse("name:detail", kwargs=url_slug)
    def __str__(self):
        return self.name

class property(models.Model):
    type_select = (
        ('perumahan', 'perumahan'),
        ('kavling', 'kavling'),
         ('rumah', 'rumah'),
         ('ruko','ruko'),
    )
    status_select = (
        ('sewa', 'sewa'),
        ('jual', 'jual'),
    )
    carport_select = (
        ('ada', 'ada'),
        ('tidak', 'tidak')
    )
    currency = (
        ('Jt', 'Jt'),
        ('M', 'M')
    )
    nama        = models.CharField(max_length=255)
    luas        = models.IntegerField()
    luas_bangunan       = models.IntegerField()
    k_tidur     = models.IntegerField()
    k_mandi     = models.IntegerField()
    garasi      = models.CharField(max_length=255, choices=carport_select)
    alamat      = models.CharField(max_length=255)
    map_point    = models.TextField(blank=True)
    status      = models.CharField(choices=status_select, max_length=255)
    tipe        = models.CharField(choices=type_select, max_length=255)
    Category    = models.ForeignKey(kondisi, on_delete=models.CASCADE)
    floor_plan  = models.ImageField(upload_to='property', blank=True, null=True)
    foto_utama  = models.ImageField(upload_to='property', blank=True, null=True)
    deskripsi   = HTMLField('content', blank=True)
    harga       = models.FloatField()
    Nominals    = models.CharField(choices=currency, max_length=50, default='M', null=True)
    published   = models.DateTimeField(auto_now_add=True)
    services    = models.ManyToManyField(ameneties)
    agent       = models.ForeignKey(User, on_delete=models.CASCADE)
    slug        = models.SlugField(blank=True, editable=False)
    terjual     = models.BooleanField(default=False)
    def save(self):
        self.slug = slugify(self.nama)
        super().save()
    def get_absolute_url(self):
        url_slug={'slug':self.slug}
        return reverse("detail", kwargs=url_slug)
    

    def __str__(self):
        return "{}. {}".format(self.nama, self.published)
    