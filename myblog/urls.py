from django.urls import path

from . import views
app_name = 'myblog'
urlpatterns = [
    path('', views.home, name='home'),
    path('blogs', views.blogs, name='blogs'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('<int:blog_id>/', views.blogdetails, name='blogdetails'),
]
