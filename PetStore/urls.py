"""PetStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import TemplateView
from django.contrib.auth import views
from django.contrib.auth.views import (
   password_reset, 
   password_reset_done,
   password_reset_confirm,
   password_reset_complete
)
#from registration.views import RegistrationView

admin.site.site_header='PetStore Administration'
admin.site.site_title='PetStore Administration'

urlpatterns = i18n_patterns(
    #url(r'^accounts/login/$', views.login, {'template_name': 'registration/c_login.html'}, name="login"),
    #url(r'^accounts/registering/$', RegistrationView.as_view(),{'template_name' : 'registration/c_registration_form.html'}, name="registration_register"),
    #url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),  
    #url(r'^accounts/password/reset/$', views.password_reset, {'template_name': 'registration/custom_password_reset_form.html'}, name="password_reset"),
    #url(r'^accounts/password/reset/done/$', password_reset_done,{'template_name': 'registration/custom_password_reset_done.html'}, name="password_reset_done"),
    #url(r'^accounts/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, {'template_name': 'registration/custom_password_reset_confirm.html'}, name="password_reset_confirm"),
    #url(r'^accounts/password/done/$', password_reset_complete, {'template_name': 'registration/custom_password_reset_complete.html'}, name="password_reset_complete"),
    #url(r'^accounts/',include('registration.backends.default.urls')),  
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^admin/', admin.site.urls,name='admin'),
    url(r'', include('backoffice.urls')),
    url(r'^tinymce/',include('tinymce.urls')),
    url(r'^rosetta/',include('rosetta.urls')),
    #url(r'^accounts/',include('registration.backends.default.urls')), 
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
