from django.contrib import admin

# Register your models here.
# from .models import Post
# from .models import Category
# from .models import UserProfile
from .models import Category,Post,Profile,Comment
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Comment)
# admin.site.register(Category,Post,UserProfile) cannot write