from django import forms



from .models import *
from . import widgets


class BarangForm(forms.ModelForm):
    class Meta:
        model = Barang
        widgets = {
            'kode_barang':forms.TextInput(attrs={'class':'form-control'}),
            'nama_barang':forms.TextInput(attrs={'class':'form-control'}),
            'harga_beli':forms.TextInput(attrs={'class':'form-control'}),
            'harga_jual':forms.TextInput(attrs={'class':'form-control'}),
             'perusahaan':forms.Select(attrs={'class':'form-control'}),
        }

class PerusahaanForm(forms.ModelForm):
    class Meta:
        model = Perusahaan
        widgets = {
            'kode_perusahaan':forms.TextInput(attrs={'class':'form-control'}),
            'nama_perusahaan':forms.TextInput(attrs={'class':'form-control'}),
            'alamat':forms.TextInput(attrs={'class':'form-control'}),
            'kota':forms.TextInput(attrs={'class':'form-control'}),
             'kode_pos':forms.TextInput(attrs={'class':'form-control'}),
             'no_telepon':forms.TextInput(attrs={'class':'form-control'}),
             'email':forms.TextInput(attrs={'class':'form-control'}),
             'logo': widgets.NotClearableFileInput,
        }

class StokForm(forms.ModelForm):
    class Meta:
        model = Stok
        widgets = {

            'nama_barang':forms.Select(attrs={'class':'form-control'}),
            'kategori':forms.TextInput(attrs={'class':'form-control'}),
            'satuan':forms.TextInput(attrs={'class':'form-control'}),
             'jumlah':forms.TextInput(attrs={'class':'form-control'}),

        }

class DetailTransaksiForm(forms.ModelForm):
    class Meta:
        model = DetailTransaksi
        
        fields = ['nama_kasir']
        widgets = {
            
            'nama_kasir': forms.HiddenInput(),
        }

class MulaiDetailTransaksiForm(forms.ModelForm):
	customer=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control '}))
	class Meta:
		model = DetailTransaksi
		fields = ['jenis_transaksi']
		widgets = {
			'jenis_transaksi': forms.Select(
			attrs={'class':'form-control'}
			),            
		}

class TransaksiAjaxForm(forms.ModelForm):
    class Meta:
        model = BarangTransaksi
        # exclude = ['author', 'updated', 'created', ]
        fields = ['barang','jumlah_barang']
        widgets = {
            'barang': forms.Select(
                attrs={'id': 'barang-select'}
            ),
            
        }


