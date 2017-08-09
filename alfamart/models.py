from django.db import models
from django.contrib.auth.models import User
from time import  strftime

# Create your models here.
class Perusahaan(models.Model):
    kode_perusahaan=models.CharField(max_length=5)
    nama_perusahaan=models.CharField(max_length=20)
    alamat=models.CharField(max_length=20)
    kota=models.CharField(max_length=10)
    kode_pos=models.CharField(max_length=5,blank=True,null=True)
    no_telepon=models.CharField(max_length=15)
    email=models.EmailField(max_length=20)
    logo=models.ImageField(null=True,blank=True)
	
    def __str__(self):
	return self.nama_perusahaan

class Barang(models.Model):
    kode_barang=models.CharField(max_length=6)
    nama_barang=models.CharField(max_length=20)
    harga_beli=models.IntegerField(max_length=6)
    harga_jual=models.IntegerField(max_length=6)
    perusahaan=models.ForeignKey(Perusahaan,related_name='asal')
    def __str__(self):
	return self.nama_barang

class Stok(models.Model):
    nama_barang=models.ForeignKey(Barang,related_name='barang_stok')
    kategori=models.CharField(max_length=10)
    satuan=models.CharField(max_length=5)
    jumlah=models.IntegerField(max_length=5)

class Customer(models.Model):
	JENIS_KELAMIN = (
		('L','Laki-Laki'),
		('P','Perempuan')
	)
	user = models.OneToOneField(User,null=True,blank=True)
	nama = models.CharField(max_length=100,null=True,blank=True)
	jenis_kelamin=models.CharField(max_length=1,choices=JENIS_KELAMIN,null=True,blank=True)
	tanggal_lahir=models.DateField(auto_now_add=False,null=True,blank=True)
	alamat=models.CharField(max_length=50,null=True,blank=True)
	kota=models.CharField(max_length=25,null=True,blank=True)
	kode_pos=models.CharField(max_length=5,null=True,blank=True)
	no_hp=models.CharField(max_length=12,null=True,blank=True)
	email=models.EmailField(null=True,blank=True)
	def __str__(self):
		return self.nama
	
class Kasir(models.Model):
	JENIS_KELAMIN = (
		('L','Laki-Laki'),
		('P','Perempuan')
	)
	user = models.OneToOneField(User,null=True,blank=True)
	nama = models.CharField(max_length=100,null=True,blank=True)
	jenis_kelamin=models.CharField(max_length=1,choices=JENIS_KELAMIN,null=True,blank=True)
	tanggal_lahir=models.DateField(auto_now_add=False,null=True,blank=True)
	no_hp=models.CharField(max_length=12,null=True,blank=True)
	alamat=models.CharField(max_length=50,null=True,blank=True)
	kode_pos=models.CharField(max_length=5,null=True,blank=True)
	def __str__(self):
		return self.nama

class Diskon(models.Model):
    nama_barang=models.ForeignKey(Barang,related_name='barang_diskon',null=True,blank=True)
    diskon=models.IntegerField(null=True,blank=True)
    tanggal_mulai_promo=models.DateField(null=True,blank=True)
    tanggal_selesai_diskon=models.DateField(null=True,blank=True)
    def __str__(self):
		return (" {} diskon {} %").format(self.nama_barang.nama_barang,self.diskon)

class DetailTransaksi(models.Model):
	JENIS_PEMBAYARAN = (
		('T','Tunai'),
		('K','Kartu Kredit')
	)
	jenis_transaksi=models.CharField(max_length=1,choices=JENIS_PEMBAYARAN,null=True,blank=True)
	no_faktur=models.CharField(max_length=10,null=True,blank=True)
	tanggal_transaksi=models.DateField(auto_now=True,null=True,blank=True)
	jam_transaksi=models.TimeField(auto_now=True,null=True,blank=True)
	nama_kasir=models.ForeignKey(Kasir,related_name='nama_kasir',null=True,blank=True)
	jumlah_bayar=models.IntegerField(null=True,blank=True)
	customer=models.ForeignKey(Customer,null=True,blank=True)
	
	
	def __str__(self):
		jam=str(self.jam_transaksi)
		jam=jam[0:8]
		return ("Transaksi {} pada tanggal {} jam {}").format(self.id,self.tanggal_transaksi,jam)
    

class BarangTransaksi(models.Model):
	detail=models.ForeignKey(DetailTransaksi,related_name='detail-transaksi',null=True,blank=True)
	barang=models.ForeignKey(Barang,related_name='barang_yang_diulang',null=True,blank=True)
	jumlah_barang=models.IntegerField(null=True,blank=True)
	total_harga=models.IntegerField(null=True,blank=True)
	
	def __str__(self):
		return ("{} sebanyak {} pada tanggal {} jam {} Faktur {}").format(self.barang.nama_barang,self.jumlah_barang,self.detail.tanggal_transaksi,self.detail.jam_transaksi,self.detail.id)
	

