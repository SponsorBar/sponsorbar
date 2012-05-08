from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url='/accounts/login/'), name='home'),

    url(r'', include('social_auth.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
