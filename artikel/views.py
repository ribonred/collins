from django.shortcuts import render
from django.views.generic import ListView,DetailView,UpdateView,CreateView, DeleteView
from django.urls import reverse_lazy
#load model
from .models import pengembangan
from .forms import Artikeledit
#grid pengembangan
class pengembanganListView(ListView):
    model = pengembangan
    template_name = "blog-grid.html"
    context_object_name = 'pengembangan_list'
    ordering = ['-published']
#detailpengenmbangan
class pengembanganDetailView(DetailView):
    model = pengembangan
    template_name = "blog-single.html"
    cotext_object_name = "pengembangan_detail"

class PengembanganCreateview(CreateView):
    model = pengembangan
    form_class = Artikeledit
    template_name = 'artikelcreate.html'
    success_url = reverse_lazy('home')
    success_message = "Created"
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class artikeldelete(DeleteView):
    model = pengembangan
    success_url = reverse_lazy('list')
    template_name= 'artikeldelete.html'
class artikelupdate(UpdateView):
    model = pengembangan
    form_class = Artikeledit
    template_name = 'artikelcreate.html'
    success_url = reverse_lazy('list')

    
