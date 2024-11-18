from django.db import models
from django.urls import reverse
from datetime import datetime,date
from ckeditor.fields import RichTextField
# Create your models here.
from django.contrib.auth.models import User
# for posting the blog
class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('home')
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    inquiry = models.CharField(max_length=100, default="no queries")
    profilephoto = models.ImageField(upload_to='profilepic/',default='default.jpg',blank=True,null=True)
    
    website_url = models.CharField(max_length=1300, null=True, blank=True)
    facebook_url = models.URLField(max_length=300, null=True, blank=True)  # Make nullable or provide a default
    instagram_url = models.CharField(max_length=400, null=True, blank=True)
    linkedin_url = models.CharField(max_length=130, null=True, blank=True)  # Corrected spelling

    def __str__(self):
        return str(self.user)
    def get_absolute_url(self):
       return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    # auther have the foriegn key of User one User admin have many author 
    author = models.ForeignKey(User,on_delete=models.CASCADE,default= 'user-name')
    # body = models.TextField()
    body = RichTextField(blank=True,null=True)
    author_img = models.ImageField(upload_to='media/')
    date_post = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255,default="coding")
    snippet = models.CharField(max_length=255,default='Click link above to read the blog post')
    like = models.ManyToManyField(User,related_name='blog_post')
    def  total_like(self):
        return self.like.count()
    def __str__(self):
        return self.title    +"   |   " +    str(self.author)
    # def get_absolute_url(self):
    #     return reverse('details',args=str(self.id))
    def get_absolute_url(self):
        return reverse('home')
    # def get_absolute_url(self):
    #     return reverse('details')
    
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name= 'do_comment')
    name = models.CharField(max_length=255)
    body = models.TextField()
    add_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '%s - %s' % (self.post.title,self.name)