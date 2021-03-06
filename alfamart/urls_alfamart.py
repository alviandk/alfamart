from django.conf.urls import patterns, include, url
from django.contrib import admin

from alfamart import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),



    # url(r'^$', views.home, name='home'),


    url(r'^input-perusahaan/$', views.PerusahaanInputView.as_view(),name='input-perusahaan'),

    # url(r'^edit-perusahaan/(?P<pk>\d+)/$', views.PerusahaanUpdateView.as_view(),name='edit-perusahaan'),
    #
    # url(r'^detail-perusahaan/(?P<pk>\d+)/$', views.PerusahaanDetailView.as_view(),name='detail-perusahaan',),
    #
    # url(r'^all-perusahaan/$', views.PerusahaanAllView.as_view(),name='all-perusahaan'),
    #

    url(r'^input-barang/$', views.BarangInputView.as_view(),name='input-barang'),

    # url(r'^edit-barang/(?P<pk>\d+)/$', views.BarangUpdateView.as_view(),name='edit-barang'),
    #
    # url(r'^detail-barang/(?P<pk>\d+)/$', views.BarangDetailView.as_view(),name='detail-barang',),
    #
    # url(r'^all-barang/$', views.BarangAllView.as_view(),name='all-barang'),
    #

	url(r'^input-stok/$', views.StokInputView.as_view(),name='input-stok'),

    # url(r'^edit-stok/(?P<pk>\d+)/$', views.StokUpdateView.as_view(),name='edit-stok'),
    #
    # url(r'^detail-stok/(?P<pk>\d+)/$', views.StokDetailView.as_view(),name='detail-stok',),
    #
    # url(r'^all-stok/$', views.StokAllView.as_view(),name='all-stok'),
    #
    #
    url(r'^transaksi/$', views.TransaksiView.as_view(),name='transaksi'),
    #
    # url(r'^transaksi-ajax/$', views.transaksi_ajax, name='transaksi-ajax'),
    #
    url(r'^transaksi-mulai/(?P<id>\d+)/$', views.TransaksiMulaiView.as_view(id=None),name='transaksi-mulai'),
    #
    # url(r'^detail-transaksi/(?P<pk>\d+)/$', views.TransaksiDetailView.as_view(),name='detail-transaksi',),
    #
    # url(r'^all-transaksi/$', views.TransaksiAllView.as_view(),name='all-transaksi'),
    #
    #
)
