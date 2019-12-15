from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, signupform, profiles
from .models import Profile
from django.views.generic import CreateView,DetailView,UpdateView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.urls import reverse_lazy
# Create your views here.

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, f"welcome {user.username}")
                    return redirect('/')
                else:
                    messages.error(request, f"password atau username tidak cocok")
            else:
                messages.error(request, f"password atau username tidak cocok")
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

#####signup
class signup(SuccessMessageMixin,CreateView):
    template_name = 'registration/regristration.html'
    form_class = signupform
    success_message = "user created, silahkan login"
    success_url = reverse_lazy('login')
    def form_valid(self, form):
        c = {'form':form, }
        user = form.save(commit=False)
        no_tlp = form.cleaned_data['no_tlp']
        foto_profile = form.cleaned_data['foto_profile']
        password = form.cleaned_data['password']
        repeat_password = form.cleaned_data['repeat_password']
        if password != repeat_password:
            messages.error(self.request,"password tidak cocok", extra_tags='alert alert-danger')
            return render(self.request, self.template_name, c)
        user.set_password(password)
        user.save()

        Profile.objects.create(user=user, no_tlp=no_tlp, foto_profile=foto_profile)
        return super(CreateView, self).form_valid(form)

