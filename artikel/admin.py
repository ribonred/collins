from django.contrib import admin
# Register your models here.
from .models import pengembangan, perijinan
class pengembanganAdmin(admin.ModelAdmin):
	readonly_fields=[
		'slug',
		'published',
        'updated',
	]

admin.site.register(pengembangan, pengembanganAdmin)
admin.site.register(perijinan)

