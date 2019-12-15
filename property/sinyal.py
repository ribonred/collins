from django.db.models.signals  import post_save, pre_save
from django.dispatch import  receiver
from .models import Customer
import requests


@receiver(pre_save, sender=Customer)
def notifysend(sender,instance, **kwargs):
    nama = instance.nama
    uid = instance.No_id
    tlp = instance.Notlp
    obj = instance.kirim_notifikasi
    url = "https://panel.rapiwha.com/send_message.php"
    querystring = {"apikey":"5RLH8KHW8I12ME62YE7N","number":"+62"+str(tlp),
    "text":"Hi *"+ str(nama) +
    "* progress dokumenmu sudah terupdate, untuk melihatnya silahkan kunjungi.. \n⬇\n*http://www.collins-property.com/kontrak/?q="+
    str(uid)+"*"
     '\n\n\n' "*ini adalah pesan otomatis yang tidak bisa di balas*"}
    if obj == True:
        response = requests.request("GET", url, params=querystring)
        print(response.text)
 