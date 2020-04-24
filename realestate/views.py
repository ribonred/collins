from django.http import HttpResponse
from django.shortcuts import render, redirect
from property.models import property, Customer
from django.views.generic import ListView,TemplateView,DetailView
from marketing.models import imagePromo,promosi,ImageFrontpage
from artikel.models import pengembangan
from django.db.models import Q
from django.core.paginator import Paginator
    
class indexListView(ListView):
    model = property
    template_name = 'index.html'
    context_object_name = 'post'
    ordering = ['-published']
    paginate_by = 4
    paginate_promo_by = 4
    paginate_artikel_by = 4
    def get_context_data(self, **kwargs):
        context = super(indexListView, self).get_context_data(**kwargs)
        p = Paginator(imagePromo.objects.select_related().all().order_by('-published'), self.paginate_promo_by)
        p2 = Paginator(pengembangan.objects.select_related().all().order_by('-published'), self.paginate_artikel_by)
        context['prom'] = p.page(context['page_obj'].number)
        context['article'] = p2.page(context['page_obj'].number)
        context['fpage'] = ImageFrontpage.objects.all()
        return context
class contactTemplateView(TemplateView):
    template_name = 'contact.html'
class permitTemplateView(TemplateView):
    template_name = 'permit.html'
class kontraktorTemplateView(ListView):
    model = Customer
    template_name = 'kontraktor.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        if query:
            object_list = Customer.objects.filter(
                Q(No_id=query)
            )
            return object_list
class loginTemplateView(TemplateView):
    template_name = 'login.html'
class original(TemplateView):
    template_name = 'original.html'