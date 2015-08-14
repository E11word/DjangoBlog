"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from liublog.views import  index,archive,articlepage,articlecategory,\
    articletag,articlecomment,loginin,register,message,loggout


urlpatterns = [
    url(r'^$',index,name='index'),
    url(r'^archive/$',archive,name='archive'),
    url(r'^articlepage/$',articlepage,name='articlepage'),
    url(r'^articlecategory/$',articlecategory,name='articlecategory'),
    url(r'^articletag/$',articletag,name='articletag'),
    url(r'^articlecomment/$',articlecomment,name='articlecomment'),
    url(r'^loginin/$',loginin,name='loginin'),
    url(r'^register/$',register,name='register'),
    url(r'^message/$',message,name='message'),
    url(r'^loggout/$',loggout,name='loggout'),
]
