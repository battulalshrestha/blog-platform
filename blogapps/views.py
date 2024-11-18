from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from .forms import Postform
from .forms import EditForm
from .models import Category,Comment
from django.http  import HttpResponseRedirect
from django.urls import reverse

# get object 404 means get this object or return 404 error | i.e page not found
# def Likeview(request,pk):
#     post = get_object_or_404(Post, id = request.POST.get('post_id'))
#     # when python manage.py dbshell is hit on terminal we and .tables and .header on | .mode column | pragma table_info("the_blog_likes"). you can find the id, post_id, user.id after only installing sqlite3
#     post.like.add(request.user)
#     return HttpResponseRedirect(reverse('details', args=[str(pk)]))

from django.urls import reverse_lazy
def Likeview(request,pk):
    post = get_object_or_404(Post, id = pk)
    # when python manage.py dbshell is hit on terminal we and .tables and .header on | .mode column | pragma table_info("the_blog_likes"). you can find the id, post_id, user.id after only installing sqlite3
    liked = False
    if post.like.filter(id = request.user.id).exists():
      post.like.remove(request.user)
      liked = False
    else:
       post.like.add(request.user)
       liked = True
    return HttpResponseRedirect(reverse('details', args=[str(pk)]))



# def Likeview(request, pk):
#     # Use the `pk` from the URL directly
#     post = get_object_or_404(Post, id=pk)

#     # Toggle the like: add if not liked, remove if already liked
#     if request.user in post.like.all():
#         post.like.remove(request.user)
#     else:
#         post.like.add(request.user)

#     return HttpResponseRedirect(reverse('details', args=[str(pk)]))

# Create your views here.
# def home(request):
#     return render(request,'index.html')
class HomeView(ListView):
   model = Post
   template_name = 'hello.html'
   ordering = ['-date_post']
   # ordering = ['-id']
   def get_context_data(self, *args, **kwargs):
      cat_menu = Category.objects.all()
      context = super(HomeView,self).get_context_data(*args,**kwargs)
      context['cat_menu'] = cat_menu
      return context
def CategoryListview(request):
      cat_menu_item= Category.objects.all()
      return render(request,'category_list.html',{'cat_menu_item':cat_menu_item})
#    context_object_name = 'posts'
class BlogdetailView(DetailView):
   model =Post
   template_name = 'details.html'
   def get_context_data(self, *args, **kwargs):
      cat_menu = Category.objects.all()
      context = super(BlogdetailView,self).get_context_data(*args,**kwargs)
      stuff = get_object_or_404(Post, id = self.kwargs['pk'])
      total_like = stuff.total_like()
      liked = False
      if stuff.like.filter(id= self.request.user.id).exists:
         liked = True
      context['cat_menu'] = cat_menu
      context['total_like'] = total_like 
      context['liked'] = liked
      return context

# it sound like the something crate view
class addCreateView(CreateView):
   model = Post
   form_class = Postform
   template_name = "add_post.html"
   success_url = reverse_lazy('home')
   def get_context_data(self, *args, **kwargs):
      cat_menu = Category.objects.all()
      context = super(addCreateView,self).get_context_data(*args,**kwargs)
      context['cat_menu'] = cat_menu
      return context
def Categoryview(request,cat):
      category_post = Post.objects.filter(category =cat.replace('-',' '))
      return render(request,'category.html',{'cat':cat.replace('-',' '),'category_post':category_post})
   
class addCategory(CreateView):
   model = Category
   # form_class = Postform
   template_name = "add_category.html"
   fields = '__all__'
   def get_context_data(self, *args, **kwargs):
      cat_menu = Category.objects.all()
      context = super(addCategory,self).get_context_data(*args,**kwargs)
      context['cat_menu'] = cat_menu
      return context
   # fields = "__all__"
   # ''' if you can not take all of the model then go from it
   # fields = ('title','body')'''


# for the editing the post i have been created4/

class addComment(CreateView):
   model = Comment
   # form_class = Postform
   template_name = "add_comment.html"
   fields = '__all__'
class UpdatePost(UpdateView):
   model = Post
   form_class = EditForm
   template_name = "update_post.html"
   def get_context_data(self, *args, **kwargs):
      cat_menu = Category.objects.all()
      context = super(UpdatePost,self).get_context_data(*args,**kwargs)
      context['cat_menu'] = cat_menu
      return context

class DeletePost(DeleteView):
   model = Post
   template_name = 'delete_post.html'
   success_url = reverse_lazy('home')
   # def get_context_data(self, *args, **kwargs):
   #    cat_menu = Category.objects.all()
   #    context = super(HomeView,self).get_context_data(*args,**kwargs)
   #    context['cat_menu'] = cat_menu
   #    return context