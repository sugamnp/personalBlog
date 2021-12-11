from django.shortcuts import render
from .models import Post
from datetime import datetime,date,timedelta

# Create your views here.
def home(request):
    editors_pick =  Post.objects.filter(editors_choice=True)[:5]
    first_editors_body = editors_pick[0].blog_body[:80]+"...."
    featured_blog = Post.objects.get(blog_feature=True)
    featured_blog_date = featured_blog.blog_created_at
    featured_blog_image = featured_blog.blog_image
    featured_blog_title = featured_blog.blog_title
    featured_blog_writer = featured_blog.blog_writer

    try:
        recent_blogs = Post.objects.filter()[::-1][:4]
    except:
        pass

    stuff_for_frontend = {
                'featured_blog_title':featured_blog_title,
                'featured_blog_writer':featured_blog_writer,
                'featured_blog_image':featured_blog_image,
                'featured_blog_date':featured_blog_date,
                'editors_pick':editors_pick,
                'first_editors_body':first_editors_body,
                'recent_blogs':recent_blogs,

    }
    return render(request, 'base.html',stuff_for_frontend)

def blogs(request):
    return render(request, 'myblog/blogdetails.html')

def aboutus(request):
    return render(request, 'myblog/blogdetails.html')

def contact(request):
    return render(request, 'myblog/contact.html')
