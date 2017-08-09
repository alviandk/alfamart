import simplejson as json
import numpy as np
from numpy import linalg as LA
from decimal import Decimal as D


from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import View, UpdateView


from .forms import *
from .models import *
# Create your views here.
def home(request):
    return render(request,'home.html')

class InputKriteriaAHPView(View):
    template_name = 'ahp/input-kri.html'
    def get(self,request):

        form = AHPKriteriaForm()
        return render(request,self.template_name,{'form':form})

    def post(self,request):

        form = AHPKriteriaForm(request.POST or None)
        if form.is_valid():
            ahp=form.save(commit=False)
            kri_umur_gaji=form.cleaned_data['kriteria_umur_gaji']
            kri_umur_luas=form.cleaned_data['kriteria_umur_luas']
            kri_gaji_luas=form.cleaned_data['kriteria_gaji_luas']
            kriteria=[]
            kriteria.append(kri_umur_gaji),kriteria.append(kri_umur_luas),kriteria.append(kri_gaji_luas)
            ahp.kri= json.dumps(kriteria)
            ahp.save()
            messages.success(request,'AHP has been successfully saved')
            return HttpResponseRedirect(reverse('input-ahp', kwargs={'id':ahp.id}))
        else:
            messages.error(request,'An error has occured, please try again')
            return render(request,self.template_name,{'form':form})

class InputAHPView(View):
    template_name = 'ahp/input-ahp.html'
    id = None
    def get(self, request, id):
        ahp = Alternatif.objects.get(id=id)
        form = AHPForm(instance=ahp)
        return render(request,self.template_name,{'form':form,'ahp':ahp})

    def post(self, request, id=None):
        ahp_ob = Alternatif.objects.get(id=id)
        form = AHPForm(request.POST, instance=ahp_ob)
        if form.is_valid():
            ahp=form.save(commit=False)
            gaji_a=form.cleaned_data['gaji_a']
            gaji_b=form.cleaned_data['gaji_b']
            gaji_c=form.cleaned_data['gaji_c']
            gaji=[]
            gaji.append(gaji_a),gaji.append(gaji_b),gaji.append(gaji_c)
            ahp.gaji= json.dumps(gaji)
            umur_a=form.cleaned_data['umur_a']
            umur_b=form.cleaned_data['umur_b']
            umur_c=form.cleaned_data['umur_c']
            umur=[]
            umur.append(umur_a),umur.append(umur_b),umur.append(umur_c)
            ahp.umur= json.dumps(umur)
            luas_a=form.cleaned_data['luas_rumah_a']
            luas_b=form.cleaned_data['luas_rumah_b']
            luas_c=form.cleaned_data['luas_rumah_c']
            luas=[]
            luas.append(luas_a),luas.append(luas_b),luas.append(luas_c)
            ahp.luas= json.dumps(luas)
            ahp.save()
            messages.success(request,'AHP has been successfully saved')
            return HttpResponseRedirect(reverse('detail-ahp', kwargs={'id':ahp.id}))
        else:
            messages.error(request,'An error has occured, please try again')
            return render(request,self.template_name,{'form':form})

RI = (0, 0, D('0.58'), D('0.9'), D('1.12'),
      D('1.24'), D('1.32'), D('1.41'), D('1.45'), D('1.49'),
      D('1.51'), D('1.48'), D('1.56'), D('1.57'), D('1.59')
)
def calculateConsistency(arr):

   eva = max(LA.eig(arr)[0]).real
   n = len(arr)
   CI = (eva-n) / (n-1)

   return CI / float(RI[n])


def calculateWeights(arr, rounding=4):

   PLACES = D(10) ** -(rounding)
   evas, eves = LA.eig(arr)
   eva = max(evas)
   eva_idx = evas.tolist().index(eva)
   eve = eves.take((eva_idx,), axis=1)
   normalized = eve / sum(eve)
   vector = [abs(e[0]) for e in normalized]
   arr= [ D( v ).quantize(PLACES) for v in vector ]
   return arr

def calculateWeightsmin(arr, rounding=4):

   PLACES = D(10) ** -(rounding)
   evas, eves = LA.eig(arr)
   eva = min(evas)
   eva_idx = evas.tolist().index(eva)
   eve = eves.take((eva_idx,), axis=1)
   normalized = eve / sum(eve)
   vector = [abs(e[0]) for e in normalized]
   arr= [ D( v ).quantize(PLACES) for v in vector ]
   return arr

class DetailAHPView(View):
    template_name = 'ahp/hasil-ahp.html'
    id = None
    def get(self,request,id=None):
        alternatif = Alternatif.objects.get(id=id)
        jsonDec = json.decoder.JSONDecoder()


        gaji = jsonDec.decode(alternatif.gaji)
        gaji_a=float(gaji[0])
        gaji_b=float(gaji[1])
        gaji_c=float(gaji[2])
        gaji_arr=np.array([gaji_a/gaji_a,gaji_b/gaji_a,gaji_c/gaji_a,
                           gaji_a/gaji_b,gaji_b/gaji_b,gaji_c/gaji_b,
                           gaji_a/gaji_c,gaji_b/gaji_c,gaji_c/gaji_c])
        gaji_arr=gaji_arr.reshape(3,3)

        gaji_arr=calculateWeights(gaji_arr)

        gaji_arr_a=gaji_arr[0]
        gaji_arr_b=gaji_arr[1]
        gaji_arr_c=gaji_arr[2]

        gaji_arr=np.array(gaji_arr)
        gaji_arr=gaji_arr.reshape(3,1)


        umur = jsonDec.decode(alternatif.umur)
        umur_a=float(umur[0])
        umur_b=float(umur[1])
        umur_c=float(umur[2])
        umur_arr=np.array([umur_a/umur_a,umur_b/umur_a,umur_c/umur_a,
                           umur_a/umur_b,umur_b/umur_b,umur_c/umur_b,
                           umur_a/umur_c,umur_b/umur_c,umur_c/umur_c])
        umur_arr=umur_arr.reshape(3,3)

        umur_arr=calculateWeights(umur_arr)
        umur_arr_a=umur_arr[0]
        umur_arr_b=umur_arr[1]
        umur_arr_c=umur_arr[2]

        umur_arr=np.array(umur_arr)
        umur_arr=umur_arr.reshape(3,1)

        luas = jsonDec.decode(alternatif.luas)
        luas_a=float(luas[0])
        luas_b=float(luas[1])
        luas_c=float(luas[2])
        luas_arr=np.array([luas_a/luas_a,luas_b/luas_a,luas_c/luas_a,
                           luas_a/luas_b,luas_b/luas_b,luas_c/luas_b,
                           luas_a/luas_c,luas_b/luas_c,luas_c/luas_c])
        luas_arr=luas_arr.reshape(3,3)

        luas_arr=calculateWeights(luas_arr)

        luas_arr_a=luas_arr[0]
        luas_arr_b=luas_arr[1]
        luas_arr_c=luas_arr[2]

        luas_arr=np.array(luas_arr)
        luas_arr=luas_arr.reshape(3,1)

        kri = jsonDec.decode(alternatif.kri)
        kri_a=float(kri[0])
        kri_b=float(kri[1])
        kri_c=float(kri[2])
        kri_arr=np.array([1,kri_a,kri_b,
                           1/kri_a,1,kri_c,
                           1/kri_b,1/kri_c,1])
        kri_arr=kri_arr.reshape(3,3)
        cons=calculateConsistency(kri_arr)


        kri_arr=calculateWeights(kri_arr)
        kri_umur=kri_arr[0]
        kri_gaji=kri_arr[1]
        kri_luas=kri_arr[2]

        kri_arr=np.array(kri_arr)
        kri_arr=kri_arr.reshape(3,1)

        alt=np.concatenate((umur_arr, gaji_arr), axis=1)
        alt=np.concatenate((alt, luas_arr), axis=1)
        alt=alt.reshape(3,3)
        hasil=np.dot(alt,kri_arr)

        bapak_a=float(hasil[0])
        bapak_b=float(hasil[1])
        bapak_c=float(hasil[2])

        maks=np.amax(hasil)
        maks=np.array(maks)
        hasil=hasil.tolist()
        inde=hasil.index(maks)
        bapak=['Bapak A','Bapak B', 'Bapak C']

        return render(request,self.template_name,{'gaji_a':int(gaji_a),'gaji_b':int(gaji_b),'gaji_c':int(gaji_c),
                                                  'umur_a':int(umur_a),'umur_b':int(umur_b),'umur_c':int(umur_c),
                                                  'luas_a':int(luas_a),'luas_b':int(luas_b),'luas_c':int(luas_c),
                                                  'bobot_gaji_a':gaji_arr_a,'bobot_gaji_b':gaji_arr_b,'bobot_gaji_c':gaji_arr_c,
                                                  'bobot_umur_a':umur_arr_a,'bobot_umur_b':umur_arr_b,'bobot_umur_c':umur_arr_c,
                                                  'bobot_luas_a':luas_arr_a,'bobot_luas_b':luas_arr_b,'bobot_luas_c':luas_arr_c,
                                                  'kri_a':int(kri_a),'kri_b':int(kri_b),'kri_c':int(kri_c),
                                                  'bobot_umur':kri_umur,'bobot_gaji':kri_gaji,'bobot_luas':kri_luas,

                                                  'bapak_a':bapak_a,'bapak_b':bapak_b,'bapak_c':bapak_c,
                                                  'bapak_max':bapak[inde],'cons':cons,'cons_pre':cons*100
                                                    })