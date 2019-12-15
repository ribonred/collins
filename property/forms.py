from django import forms
from .models import property, Customer,uangmuka,ProsesBangun
from django.forms import CheckboxSelectMultiple,widgets
from django.forms.models import inlineformset_factory

class proper(forms.ModelForm): 
    class Meta:
        model = property
        fields = ('__all__')
        exclude = ('agent',)
class CreateCs(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('nama','alamat','Notlp', 'No_id',)
class UpdateCs(forms.ModelForm):
    class Meta:
        model = Customer
        exclude =('user',)
        widgets = {
            'Booking_Date': forms.DateInput(
                attrs={
                    'id':'datepickers'
                }
            ),
            'tgl_persetujuan_prinsip': forms.DateInput(
                attrs={
                    'id':'prinsip'
                }
            ),
            'tgl_sp3k': forms.DateInput(
                attrs={
                    'id':'sp3k'
                }
            ),
            'tgl_persetujuan': forms.DateInput(
                attrs={
                    'id':'persetujuan'
                }
            ),
            'tgl_realisasi': forms.DateInput(
                attrs={
                    'id':'realisasi'
                }
            ),
            'tgl_serah_terima': forms.DateInput(
                attrs={
                    'id':'serahterima'
                }
            ),
        }
class UangMuka(forms.ModelForm):
    class Meta:
        model = uangmuka
        exclude = ()

class prosesbangunform(forms.ModelForm):
    class Meta:
        model = ProsesBangun
        exclude = ()



updatecsformset = inlineformset_factory(Customer,uangmuka,form=UangMuka,fields=['jumlah','keterangan', 'tgl_byr'],extra=1, can_delete=True)
pbangunformset = inlineformset_factory(Customer,ProsesBangun,form=prosesbangunform,fields=['foto', 'keterangan','tgl'],extra=1, can_delete=True)