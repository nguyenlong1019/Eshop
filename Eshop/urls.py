from django.contrib import admin
from django.urls import path  , include, re_path
from django.conf.urls.static import static
from django.views.static import serve
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('store.urls')),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'store.views.page404.handling404'