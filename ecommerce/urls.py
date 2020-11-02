"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.master),
    path('login/',views.login),
    path('usrhome/', views.master),
    path('profile/', views.profile),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('mobile',views.mobile),
    path('laptop/',views.laptop),
    path('pdetail/<int:id>',views.pdetail),
    path('idetail/<int:id>',views.idetail),
    path('sdetail/<int:id>',views.sdetail),
    path('shoedetail/<int:id>',views.shoedetail),
    path('wdetail/<int:id>',views.wdetail),
    path('shdetail/<int:id>',views.shdetail),
    path('delldetail/<int:id>',views.delldetail),
    path('jdetail/<int:id>',views.jdetail),
    path('hpdetail/<int:id>',views.hpdetail),
    path('ldetail/<int:id>',views.ldetail),
    path('mens',views.mens),
    path('logout/',views.logout),
    path('delete/<int:id>',views.delete),
    path('mail/',views.mail),
    path('about/',views.about),
    path('forget/',views.forget),
    path('contact/',views.contact),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
