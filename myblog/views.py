from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'base.html')

def blogs(request):
    return render(request, 'myblog/blogdetails.html')

def aboutus(request):
    return render(request, 'myblog/blogdetails.html')

def contact(request):
    return render(request, 'myblog/contact.html')
