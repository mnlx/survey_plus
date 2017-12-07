"""tango_with_django_project URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include

from registration.backends.simple.views import RegistrationView





class MyRegView(RegistrationView):
    def get_success_url(self, user=None):
        return '/forms/'

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    #bellow related to rango app

    # url(r'^$', views.index, name='index'),
    # url(r'^rango/', include('rango.urls')),
    url(r'^accounts/register/$', MyRegView.as_view(),name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    # url(r'^conversations/', include('conversations.urls')),
    url(r'^forms/', include('forms.urls')),
    # url(r'^analise/', include('analise.urls')),
]


urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
