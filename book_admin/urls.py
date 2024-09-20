"""book_admin URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from app01 import views

urlpatterns = [
    url(r'^index.html', views.index, name='index'),
    url(r'^admin/', admin.site.urls),

    url(r'^add_publish.html$', views.add_publish, name='add_publish'),
    url(r'^publish_list.html$', views.publish_list, name='publish_list'),
    url(r'^del_publish/(\d+).html$', views.del_publish),
    url(r'^edit_publish/(\d+).html$', views.edit_publish, name='edit_publish'),

    url(r'^add_book.html$', views.add_book, name='add_book'),
    url(r'^book_list.html$', views.book_list, name='book_list'),
    url(r'^del_book/(\d+).html$', views.del_book),
    url(r'^edit_book/(\d+).html$', views.edit_book, name='edit_book'),

    url(r'^add_author.html$', views.add_author, name='add_author'),
    url(r'^author_list.html$', views.author_list, name='author_list'),
    url(r'^del_author/(\d+).html$', views.del_author),
    url(r'^edit_author/(\d+).html$', views.edit_author, name='edit_author'),

]
