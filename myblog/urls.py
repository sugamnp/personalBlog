from django.urls import path

from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('blogs', views.blogs, name='blogs'),
    path('aboutus', views.blogs, name='aboutus'),
    path('contact', views.blogs, name='contact'),

]
