from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings
# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'blog.views.home_page', name='home'),
    url(r'^refresh_captcha$', 'comment.views.refresh_captcha', name='refresh_captcha'),

    url(r'^blog/', include('blog.urls')),
    url(r'^comment/', include('comment.urls')),
    # url(r'^kliyes_blog/', include('kliyes_blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^captcha/', include('captcha.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns("",
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}
        ),
    )
