"""realestate URL Configuration

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
from django.urls import path
from django.conf import settings
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from .views import indexListView,contactTemplateView, permitTemplateView,kontraktorTemplateView,loginTemplateView,original

urlpatterns = [
    path('marketing/',include('marketing.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    path('product/',include('property.urls')),
    path('artikelpengembangan/', include('artikel.urls')),
    path('admin/', admin.site.urls),
    path("", indexListView.as_view(), name='home'),
    path("contact/", contactTemplateView.as_view(), name='contact'),
    path("permit/", permitTemplateView.as_view(), name="permit"),
    path("kontrak/", kontraktorTemplateView.as_view(), name="kontrak"),
    path('acount/', include('acount.urls')),
    path("ori/", original.as_view(), name="ori"),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT )
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)