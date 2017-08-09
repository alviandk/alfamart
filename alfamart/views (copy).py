import json
from datetime import date


from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import View, UpdateView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.db.models import Sum

from .form import *

class InsideView(View):

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(InsideView, self).dispatch(request, *args, **kwargs)


@login_required
def home(request):
    return render(request,'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))
            else:
                #redirect to disable account msg
                messages.error(request,'Ah, account anda tidak aktif :(')
                return HttpResponseRedirect(reverse('login'))
        else:
            #invalid login
            messages.error(request,'Tetot, coba lagi!')
            return HttpResponseRedirect(reverse('login'))

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))



class BarangInputView(InsideView, View):
    template_name = 'barang/input-barang.html'
    def get(self,request):

        form = BarangForm()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = BarangForm(request.POST or None)
        if form.is_valid():
            input_barang = form.save(commit=False)
            input_barang.save()

            messages.success(request,'Barang telah selesai diinput')
            return HttpResponseRedirect(reverse('all-barang'))
        else:
            messages.error(request,'Terjadi error, coba lagi')
            return render(request,self.template_name,{'form':form})

class BarangUpdateView(InsideView,UpdateView):

    model = Barang
    template_name = 'barang/update-barang.html'
    form_class = BarangForm

    def get_success_url(self):
        return reverse('all-barang')

    def get_context_data(self, **kwargs):

        context = super(BarangUpdateView, self).get_context_data(**kwargs)
        context['action'] = reverse('edit-barang', kwargs={'pk': self.get_object().id})

        return context

class BarangDetailView(InsideView,DetailView):
    model = Barang
    template_name = 'barang/detail-barang.html'

class BarangAllView(InsideView,View):
    template_name = 'barang/all-barang.html'

    def get(self,request):
        barang = Barang.objects.all()

        return render(request,self.template_name,{'barang':barang})

class PerusahaanInputView(InsideView,View):
    template_name = 'perusahaan/input-perusahaan.html'
    def get(self,request):
        form = PerusahaanForm()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = PerusahaanForm(request.POST or None)
        if form.is_valid():
            input_perusahaan = form.save(commit=False)
            input_perusahaan.save()

            messages.success(request,'Data Perusahaan telah selesai diinput')
            return HttpResponseRedirect(reverse('all-perusahaan'))
        else:
            messages.error(request,'Terjadi error, coba lagi')
            return render(request,self.template_name,{'form':form})

class PerusahaanUpdateView(InsideView,UpdateView):

    model = Perusahaan
    template_name = 'perusahaan/update-perusahaan.html'
    form_class = PerusahaanForm

    def get_success_url(self):
        return reverse('all-perusahaan')

    def get_context_data(self, **kwargs):

        context = super(PerusahaanUpdateView, self).get_context_data(**kwargs)
        context['action'] = reverse('edit-perusahaan', kwargs={'pk': self.get_object().id})

        return context

class PerusahaanDetailView(InsideView,DetailView):
    model = Perusahaan
    template_name = 'perusahaan/detail-perusahaan.html'

class PerusahaanAllView(InsideView,View):
    template_name = 'perusahaan/all-perusahaan.html'

    def get(self,request):
        perusahaan = Perusahaan.objects.all()

        return render(request,self.template_name,{'perusahaan':perusahaan})


class StokInputView(InsideView,View):
    template_name = 'stok/input-stok.html'
    def get(self,request):
        form = StokForm()
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form = StokForm(request.POST or None)
        if form.is_valid():
            input_stok = form.save(commit=False)
            input_stok.save()

            messages.success(request,'Stok telah selesai diinput')
            return HttpResponseRedirect(reverse('all-stok'))
        else:
            messages.error(request,'Terjadi error, coba lagi')
            return render(request,self.template_name,{'form':form})

class StokUpdateView(InsideView,UpdateView):

    model = Stok
    template_name = 'stok/update-stok.html'
    form_class = StokForm

    def get_success_url(self):
        return reverse('all-stok')

    def get_context_data(self, **kwargs):

        context = super(StokUpdateView, self).get_context_data(**kwargs)
        context['action'] = reverse('edit-stok', kwargs={'pk': self.get_object().id})

        return context

class StokDetailView(InsideView,DetailView):
    model = Stok
    template_name = 'stok/detail-stok.html'

class StokAllView(InsideView,View):
    template_name = 'stok/all-stok.html'

    def get(self,request):
        stok = Stok.objects.all()

        return render(request,self.template_name,{'stok':stok})


class TransaksiView(InsideView,View):
	template_name='transaksi/transaksi.html'
	def get(self,request):
		
		
		return render(request,self.template_name)
	
	def post(self,request):
		form = DetailTransaksiForm(request.POST or None)
		kasir = Kasir.objects.get(user=request.user.id)
		if form.is_valid():
			transaksi=form.save(commit=False)
			transaksi.nama_kasir=kasir
			sekarang=date.today()
			sekarang=sekarang.isoformat()
			transaksi.tanggal_transaksi=sekarang
			
			transaksi.save()
		
		return HttpResponseRedirect(reverse('transaksi-mulai', kwargs={'id': transaksi.id}))

class TransaksiMulaiView(InsideView,View):
	template_name='transaksi/transaksi-mulai.html'
	id = None
	
	def get(self, request, id):
		transaksi = DetailTransaksi.objects.get(id=id)
		
		
		form=MulaiDetailTransaksiForm(instance=transaksi,initial={'id':transaksi.id,})	
		form_ajax=TransaksiAjaxForm()
		barang=BarangTransaksi.objects.filter(detail=transaksi)
		sekarang=date.today()
		diskon=Diskon.objects.filter(Q(tanggal_mulai_promo__lte=sekarang) & Q(tanggal_selesai_diskon__gt=sekarang))
		
		
		
		return render(request,self.template_name,{'transaksi':transaksi,'form':form,'barang':barang,'form_ajax':form_ajax,'diskon':diskon})
		
	def post(self,request,id=None):
		transaksi = DetailTransaksi.objects.get(id=id)		
		form = MulaiDetailTransaksiForm(request.POST,instance=transaksi)
		form_ajax = TransaksiAjaxForm(request.POST or None)	
		
		if form.is_valid():
			transaksi_form=form.save(commit=False)
			customer=form.cleaned_data['customer']
			custom=Customer.objects.get(id=customer)
			transaksi_form.customer=custom
			transaksi_form.save()	
		elif form_ajax.is_valid():
			sekarang=date.today()
			diskon=Diskon.objects.filter(Q(tanggal_mulai_promo__lte=sekarang) & Q(tanggal_selesai_diskon__gt=sekarang) )			
			transaksi_barang = form_ajax.save(commit=False)
			if Diskon.objects.get(nama_barang=transaksi_barang.barang):
				disk= Diskon.objects.get(nama_barang=transaksi_barang.barang)
			transaksi_barang.detail=transaksi
			if transaksi_barang.barang:
				if Diskon.objects.get(nama_barang=transaksi_barang.barang):
					disk= Diskon.objects.get(nama_barang=transaksi_barang.barang)
					total=form_ajax.cleaned_data['jumlah_barang']*transaksi_barang.barang.harga_jual
					transaksi_barang.total_harga=total-total*disk.diskon/100
				else:
					transaksi_barang.total_harga=form_ajax.cleaned_data['jumlah_barang']*transaksi_barang.barang.harga_jual
				
				transaksi_barang.save()
			messages.success(request,'Barang telah selesai diinput')
			
		return HttpResponseRedirect(reverse('transaksi-mulai', kwargs={'id': transaksi.id}))

def transaksi_ajax(request):
	
	if request.method == 'POST':
		barang = request.POST.get('barang')
		response_data = {}
		barang=Barang.objects.get(id=barang)
		id=barang
		transaksi = BarangTransaksi(barang=barang)
		transaksi.save()
		response_data['transaksipk'] = transaksi.pk
		response_data['nama_barang'] = transaksi.barang.nama_barang
		return HttpResponse(json.dumps(response_data),content_type="application/json")
	
	

class TransaksiDetailView(InsideView,DetailView):
    
    template_name = 'transaksi/detail-transaksi.html'

class TransaksiAllView(InsideView,View):
    template_name = 'transaksi/all-transaksi.html'

    def get(self,request):
        transaksi = DetailTransaksi.objects.all()

        return render(request,self.template_name,{'transaksi':transaksi})

class DetailTransaksiCreateView(InsideView,View):
    template_name = 'transaksi/all-transaksi.html'
    model=DetailTransaksi


