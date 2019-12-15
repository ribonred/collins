from django.urls import path
from django.conf.urls import url
from .views import (promoDetail)

urlpatterns = [
    path("",promoDetail.as_view(), name='listpromo'),
]