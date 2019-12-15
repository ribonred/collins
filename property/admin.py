from django.contrib import admin
from .models import property, kondisi, ameneties, Customer,uangmuka,ProsesBangun

from django.db import models

class kondisiAdmin(admin.ModelAdmin):
    readonly_fields=['slug']
admin.site.register(kondisi, kondisiAdmin)

class propertyAdmin(admin.ModelAdmin):
	readonly_fields=[
		'slug',
		'published',
	]
	list_display = ['nama','alamat','Category','agent','harga']
	list_editable_links = ['agent',]
	list_editable = ['agent',]

admin.site.register(property, propertyAdmin)
admin.site.register(ameneties)
admin.site.register(Customer)
admin.site.register(uangmuka)
admin.site.register(ProsesBangun)


# Register your models here.
