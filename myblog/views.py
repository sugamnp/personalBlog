from django.shortcuts import render, get_object_or_404
from .models import Post
from datetime import datetime,date,timedelta

# Create your views here.
def home(request):
    editors_pick =  Post.objects.filter(editors_choice=True)[:5]
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
                'featured_blog':featured_blog,
                'featured_blog_title':featured_blog_title,
                'featured_blog_writer':featured_blog_writer,
                'featured_blog_image':featured_blog_image,
                'featured_blog_date':featured_blog_date,
                'editors_pick':editors_pick,
                'recent_blogs':recent_blogs,

    }
    return render(request, 'base.html',stuff_for_frontend)

def blogs(request):
    all_blogs = Post.objects.filter()
    all_blogs = all_blogs[::-1]
    stuff_for_frontend = {
        'all_blogs':all_blogs,
    }

    return render(request,'myblog/blog.html',stuff_for_frontend)

def blogdetails(request, blog_id):
    blog = get_object_or_404(Post, pk=blog_id)
    stuff_for_frontend = {
            'blog':blog,
    }
    return render(request,'myblog/blogdetails.html', stuff_for_frontend)

def aboutus(request):
    return render(request, 'myblog/aboutus.html')
