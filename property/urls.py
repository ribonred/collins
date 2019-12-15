from django.urls import path
from django.conf.urls import url
from .views import (
    propertyLisView,
    propertyDetailView,
    propertyCategoryPrim,
    propertyCategorySec,
    properview,
    adminLisView,
    adminupdateview,
    admindelete,
    Csview,
    Cscreate,
    Csupdate,
    Csdelete,
    Addpromo,
    profildetail,
    profileedit,
    mapview
)

urlpatterns = [
    path("maps/", mapview.as_view(), name="mapbox"),
    path('second/',propertyCategorySec.as_view(), name='list category second'),
    path('primary/',propertyCategoryPrim.as_view(), name='list category primary'),
    path('',propertyLisView.as_view(), name='list product'),
    url(r'^detail/(?P<slug>[\w-]+)$',propertyDetailView.as_view(), name='detail'),
    path('form/add',properview.as_view(),name='admin'),
    path('form/',adminLisView.as_view(), name='adminlist'),
    path('form/edit/<int:pk>',adminupdateview.as_view(), name='admineditlist'),
    path('form/delete/<int:pk>',admindelete.as_view(), name='admindelete'),
    path('form/customer/', Csview.as_view(), name='cslist'),
    path("form/customer/create", Cscreate, name="cscreate"),
    path("form/customer/update/<int:pk>", Csupdate.as_view(), name="csupdate"),
    path("form/customer/delete/<int:pk>", Csdelete, name="csdelete"),
    path("form/promo/", Addpromo.as_view(), name="promo"),
    path("form/profile/<int:pk>", profildetail.as_view(), name="profiles"),
    path("form/profileedit/<int:pk>", profileedit.as_view(), name="editprof")
]