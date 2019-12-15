from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.db import transaction
from django.views.generic import ListView,DetailView,CreateView,TemplateView,UpdateView,DeleteView
from .forms import proper, CreateCs, UpdateCs,updatecsformset,pbangunformset
from marketing.forms import PromoForms
from marketing.models import imagePromo
from acount.models import Profile
from acount.forms import profiles
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q
#load model
from .models import kondisi, property, ameneties, Customer

class mapview(TemplateView):
    template_name= 'maps/map.html'
    def get_context_data(self, **kwargs):
        context = super(mapview, self).get_context_data(**kwargs)
        context["tokens"] = 'pk.eyJ1Ijoicmlib25yZWQxMiIsImEiOiJjazJiYmxhbWowMHV0M2JvNHowdWFrN3J2In0.J0HGhdtAAh1M7iXbriC0_w'
        return context
    
################[ LISTING ]##################################
class propertyCategorySec(ListView):
    model = property
    template_name = 'property-grid.sec.html'
    context_object_name = 'categorylist'
    queryset = property.objects.filter(Category__name ='secondary', terjual=False)
    ordering = ['-published']
    paginate_by = 6

class propertyCategoryPrim(ListView):
    model = property
    template_name = 'property-grid.prim.html'
    context_object_name = 'categorylist'
    queryset = property.objects.filter(Category__name ='primary', terjual=False)
    ordering = ['-published']
    paginate_by = 6

class propertyLisView(ListView):
    template_name = 'property-grid.html'
    context_object_name = 'product_list'
    ordering = ['-published']
    paginate_by = 20
    def get_queryset(self): # new
        queryset = property.objects.filter(terjual=False).order_by('-published')
        kmandi = self.request.GET.get('kmandi')
        ktidur = self.request.GET.get('ktidur')
        Luas = self.request.GET.get('luas')
        HRG = self.request.GET.get('hrg')
        nom = self.request.GET.get('nom')
        alamats = self.request.GET.get('alamat')
        if alamats and nom == None:
            object_list = property.objects.filter(
                Q(alamat__icontains=alamats)|
                Q(nama__icontains=alamats)
            )
            return object_list
            
        elif nom and alamats == '':
            obj = property.objects.filter(
                Q(Nominals__contains=nom)
            )
            return obj
        elif nom and alamats:
            obs = property.objects.filter(
                Q(Nominals__exact=nom),
                Q(alamat__icontains=alamats)|
                Q(nama__icontains=alamats)
            )
            return obs

        return queryset

class propertyDetailView(DetailView):
    model = property 
    template_name = "property-single.html"
    def get_context_data(self, **kwargs):
        context = super(propertyDetailView, self).get_context_data(**kwargs)
        context["gallery"] = property.objects.all()
        return context
##################[ LISTING END ]###########################

################## [ ADMIN PROPERTY ]###################
class properview(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = property
    template_name = 'add.html'
    form_class = proper
    success_url = reverse_lazy('adminlist')
    login_url = 'login'
    success_message = "Created"
    def form_valid(self, form):
        form.instance.agent = self.request.user
        return super().form_valid(form)
class adminLisView(ListView):
    template_name = 'form.html'
    context_object_name = 'listing'
    ordering = ['-published']
    paginate_by = 5
    def get_queryset(self):
        query = self.request.user.property_set.all()
        search = self.request.GET.get('q')
        if search:
            query = self.request.user.property_set.filter(
                Q(alamat__icontains=search)|
                Q(nama__icontains=search)
            )
        return query
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = Profile.objects.filter(user=self.request.user)
        return context
    
class adminupdateview(SuccessMessageMixin,UpdateView):
    model = property
    template_name = "edit.html"
    form_class = proper
    success_url = reverse_lazy('adminlist')
    success_message = "updated"
class admindelete(DeleteView):
    model = property
    success_url = reverse_lazy('adminlist')
    template_name = 'delete.html'
  ################## [ ADMIN PROPERTY END ]###################

  #################[ADMIN CUSTOMER]#######################
class Csview(LoginRequiredMixin,ListView):
    template_name = 'cs/customer.html'
    context_object_name = 'customer'
    model = Customer


def save_cs_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            data['form_is_valid'] = True
            customer = Customer.objects.all()
            data['html_book_list'] = render_to_string('cs/partcslist.html', {
                'customer': customer
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def Cscreate(request):
    if request.method == 'POST':
        form = CreateCs(request.POST)
    else:
        form = CreateCs()
    return save_cs_form(request, form, 'cs/create.html')

class Csupdate(UpdateView):
    form_class = UpdateCs
    template_name = 'cs/update.html'
    model = Customer
    success_url = reverse_lazy('adminlist')

    def get_context_data(self, **kwargs):
        data = super(Csupdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['titles'] = updatecsformset(self.request.POST, instance=self.object)
            data['pros'] = pbangunformset(self.request.POST, instance=self.object, files=self.request.FILES)
        else:
            data['titles'] = updatecsformset(instance=self.object)
            data['pros'] = pbangunformset(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        titles = context['titles']
        proses = context['pros']
        with transaction.atomic():
            self.object = form.save()
            if titles.is_valid() and proses.is_valid():
                titles.instance = self.object
                proses.instance = self.object
                titles.save()
                proses.save()
        return super(Csupdate, self).form_valid(form)
# def Csupdate(request, pk):
#     cs = get_object_or_404(Customer, pk=pk)
#     if request.method == 'POST':
#         form = UpdateCs(request.POST, instance=cs)
#     else:
#         form = UpdateCs(instance=cs)
#     return save_cs_form(request, form, 'cs/update.html')

def Csdelete(request, pk):
    cs = get_object_or_404(Customer, pk=pk)
    data = dict()
    if request.method == 'POST':
        cs.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        customer = Customer.objects.all()
        data['html_book_list'] = render_to_string('cs/partcslist.html', {
            'customer': customer
        })
    else:
        context = {'cs': cs}
        data['html_form'] = render_to_string('cs/delete.html',
            context,
            request=request,
        )
    return JsonResponse(data)
###########[END ADMIN CUSTOMER]###########################

class Addpromo(LoginRequiredMixin,SuccessMessageMixin, CreateView):
    form_class = PromoForms
    model = imagePromo
    success_url = reverse_lazy('adminlist')
    login_url = 'login'
    template_name = 'promo/promo.html'
    success_message = "Promo Created"
    def form_valid(self, form):
        form.instance.publisher = self.request.user
        return super().form_valid(form)

class profildetail(DetailView):
    model = Profile
    template_name = 'profile.html'
class profileedit(UpdateView):
    model = Profile
    template_name = 'profedit.html'
    form_class = profiles
    success_url = reverse_lazy('adminlist')