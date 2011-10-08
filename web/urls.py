from django.conf.urls.defaults import patterns, include
from django.contrib import admin
import settings
import views

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', views.main),
    (r'^digest/$', views.digest),
    (r'^pattern/(\d+)/(\d+)/$', views.show_pattern),
    (r'^data/(\d+)/(.+)/(\d+)/$', views.get_data),
    (r'^pattern/new/$', views.new_pattern),
    (r'^pattern/all/$', views.all_patterns),
    (r'^patterns/save/$', views.save_patterns),
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    from django.views.static import serve
    _media_url = settings.MEDIA_URL
    if _media_url.startswith('/'):
        _media_url = _media_url[1:]
        urlpatterns += patterns('',
                                (r'^%s(?P<path>.*)$' % _media_url,
                                 serve,
                                 {'document_root': settings.MEDIA_ROOT}))
    del(_media_url, serve)
