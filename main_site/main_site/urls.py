from django.contrib import admin
from django.urls import path
from portfolio.views import homepage, about, gallery
from django.conf import settings
from django.conf.urls.static import static # enable image content
from django.urls import include, path # auto page refresh


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', homepage, name='homepage'),
    path("about/", about, name="about"), 
    path("gallery/<slug:slug>/", gallery, name="gallery"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [path("__reload__/", include("django_browser_reload.urls"))]