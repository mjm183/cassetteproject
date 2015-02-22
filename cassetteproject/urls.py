from django.conf.urls import patterns, include, url
from django.contrib import admin
from cassetteinventory import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cassetteproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^addTape/$', views.AddTapeView),
    url(r'^addArtist/$', views.AddArtistView),
    url(r'^addLabel/$', views.AddLabelView),
    url(r'^ViewTapes/$', views.ViewTapes),

)
#Project to Archive Michael's Tapes
#Started on 02/21/15
#Kyle and Michael

