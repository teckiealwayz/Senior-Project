from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from contact import views as contact_views
from profiles import views as profile_views



urlpatterns = [

    # /admin -- database login
    url(r'^admin/', admin.site.urls),

    # /home/
    url(r'^$', profile_views.home, name='home'),

    # /about/
    url(r'^about/$', profile_views.about, name='about'),

    # contact/
    url(r'^contact/$', contact_views.contact, name='contact'),

    # authentication
    url(r'^accounts/', include('allauth.urls')),



]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)