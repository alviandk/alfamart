from django.conf.urls import patterns, include, url
from django.contrib import admin

from ahp import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.home, name='home-ahp'),

    url(r'^input-ahp/(?P<id>\d+)$', views.InputAHPView.as_view(id=None),name='input-ahp'),

    url(r'^input-kri/$', views.InputKriteriaAHPView.as_view(),name='input-kri'),

    url(r'^detail-ahp/(?P<id>\d+)$', views.DetailAHPView.as_view(id=None),name='detail-ahp'),

    #url(r'^output-ahp/(?P<pk>\d+)/$', views.UpdatePerusahaanView.as_view(),name='edit-ahp',),

    )
