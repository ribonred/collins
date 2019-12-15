from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic import ListView,DetailView, TemplateView
from .models import promosi,imagePromo

class promoDetail(TemplateView):
    template_name = 'promo.html'