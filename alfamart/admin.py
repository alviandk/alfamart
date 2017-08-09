from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Customer)
admin.site.register(Diskon)
admin.site.register(Perusahaan)
admin.site.register(Kasir)
admin.site.register(Barang)
admin.site.register(Stok)
admin.site.register(BarangTransaksi)
admin.site.register(DetailTransaksi)
