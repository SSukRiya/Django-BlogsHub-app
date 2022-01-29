from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView,DetailView, CreateView, UpdateView, ListView
from django.views.generic.edit import DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from .models import Notes
from .forms import NotesForm
from datetime import datetime


# Create your views here.
''' 
function based view

def home(request):
    return render(request,'home/home.html',{'today': datetime.now(),})

'''
# class based views


class Home(TemplateView):
    template_name='home/home.html'
    extra_context={'today': datetime.today(),}

class Authorized(LoginRequiredMixin, ListView):
    template_name='home/authorized.html'
    model=Notes
    context_object_name='notes' 

class AuthDetailView(DetailView):
    model=Notes
    context_object_name='note'
    template_name='home/authorized detail.html'
    extra_context={'today': datetime.today(),}  

class NotesListView(LoginRequiredMixin, ListView):
    model=Notes
    context_object_name='notes'
    template_name='home/list.html'
    login_url='/admin'
    def get_queryset(self):
        return self.request.user.notes.all()

class NotesDetailView(LoginRequiredMixin, DetailView):
    model=Notes
    context_object_name='note'
    template_name='home/detail.html'
    extra_context={'today': datetime.today(),}
    
class NotesNewView(LoginRequiredMixin, CreateView):
    model=Notes
    form_class = NotesForm
    template_name='home/new.html'
    success_url='/blogshub/list'
    login_url='/admin'
    def form_valid(self,form):
        self.object=form.save(commit=False)
        self.object.user=self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class NotesEditView(LoginRequiredMixin, UpdateView):
    model=Notes
    form_class = NotesForm
    context_object_name='note'
    template_name='home/edit.html'
    success_url='/blogshub/list'

class NotesDeleteView(LoginRequiredMixin, DeleteView):
    model=Notes
    template_name='home/delete.html'
    success_url='/blogshub/list'

class LoginInterfaceView(LoginView):
    template_name='home/login.html'

class LogoutInterfaceView(LogoutView):
    template_name='home/logout.html'

class SignUpView(CreateView):
    form_class=UserCreationForm
    template_name='home/register.html'
    success_url='/blogshub/login'
    def get(self,request,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request,*args,**kwargs)

