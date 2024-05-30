from django.shortcuts import render
from .models import StudentsPost

def post_list(request):
    posts = StudentsPost.objects.all()
    return render(request, 'pages/post_list.html', {'posts': posts})
def post_detail(request, pk):
    post = StudentsPost.objects.get(pk=pk)
    return render(request, 'pages/post_detail.html', {'post': post})

# Create your views here.
