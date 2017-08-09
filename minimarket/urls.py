from django.conf.urls import patterns, include, url
from django.contrib import admin
from alfamart import urls_alfamart
from alfamart import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'minimarket.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^login/$', views.login_view,name='login'),
    url(r'^$', views.login_view, name='login'),
    # url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^alfamart/',include(urls_alfamart)),
)

urlpatterns += [url(r'^silk/', include('silk.urls', namespace='silk'))]
