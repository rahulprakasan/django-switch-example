"""basicforms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.conf.urls import include
import waterapp.views
urlpatterns = [
url(r'^$',waterapp.views.index,name='index'),
   url(r'^formpage/',waterapp.views.form_name_view,name='form_name'),
url(r'^status/',include('waterapp.urls')),
##url(r'^state/',waterapp.views.status,name='state'),
url(r'^state/',waterapp.views.switch,name='state'),
    url(r'^admin/', admin.site.urls),
]
