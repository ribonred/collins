from django.urls import path
from django.conf.urls import url
from .views import (
    pengembanganListView, 
    pengembanganDetailView,
    PengembanganCreateview,
    artikeldelete,
    artikelupdate,
)

urlpatterns = [
    path('',pengembanganListView.as_view(), name='list'),
    url(r'^detail/(?P<slug>[\w-]+)$',pengembanganDetailView.as_view(), name='details'),
    path("artikelcreate/", PengembanganCreateview.as_view(), name="artikelcreate"),
    path("delartikel/<int:pk>", artikeldelete.as_view(), name="deleteartikel"),
    path("upartikel/<int:pk>", artikelupdate.as_view(), name="updateartikel"),
]
