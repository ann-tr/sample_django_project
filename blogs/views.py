from django.shortcuts import render
from .models import Blog

# Create your views here.


def model_retrieval(request):
    
    data = Blog.objects.all()
    context = {"blog_no": data}
    return render(request, 'template/home.html' , context)