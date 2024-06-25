from django.shortcuts import render , redirect
from .models import Blog
from .forms import BlogForm
# Create your views here.


'''def model_retrieval(request):
    
    data = Blog.objects.all()
    context = {"blog_no": data}
    return render(request, 'template/home.html' , context)

'''

def blog_post(request):
    #context ={}
    if request.POST :
    # create object of form
        form = BlogForm(request.POST or None ,  request.FILES or None)
        print(request.FILES)
     
    # check if form data is valid
        if form.is_valid():
        # save the form data to model
            form.save()
 
 
    #context['form']= form  
    return render(request, "template/home.html", {'form':BlogForm})