from django.shortcuts import render
from .models import StudentsPost
from django.views.generic import ListView, DeleteView, DetailView, UpdateView, CreateView
from django.urls import reverse_lazy


class StudentsCreateView(CreateView):
    model = StudentsPost
    fields = ['matricula', 'nome', 'sobrenome', 'serie', 'descricao'] 
    template_name = 'pages/post_create.html'
    success_url = '/students/'

class StudentsDetailView(DetailView):
    model = StudentsPost
    template_name = 'pages/post_detail.html'

class StudentsUpdateView(UpdateView):
    model = StudentsPost
    fields = ['matricula', 'nome', 'sobrenome', 'serie', 'descricao'] 
    template_name = 'pages/post_update.html'
    success_url = '/students/' 

class StudentsDeleteView(DeleteView):
    model = StudentsPost
    template_name = 'pages/post_delete.html'
    success_url = reverse_lazy('post_list') 

class StudentsListView(ListView):
    model =  StudentsPost
    template_name = 'pages/post_list.html'
    context_object_name = 'posts'


'''
def post_list(request):
    posts = StudentsPost.objects.all()
    return render(request, 'pages/post_list.html', {'posts': posts})
def post_detail(request, pk):
    post = StudentsPost.objects.get(pk=pk)
    return render(request, 'pages/post_detail.html', {'post': post})

# Create your views here.
'''