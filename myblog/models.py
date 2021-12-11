from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    blog_id = models.AutoField
    blog_writer = models.CharField(max_length=15, default="")
    blog_title = models.CharField(max_length=100, default ="")
    blog_body = models.CharField(max_length=1000000, default ="")
    blog_created_at = models.DateTimeField(default=datetime.now, blank=True)
    blog_image = models.ImageField(upload_to="static/images/posts" , default ="")
    blog_feature = models.BooleanField(default="False")
    editors_choice = models.BooleanField(default="False")

    def __str__(self):
        return self.blog_title
            
