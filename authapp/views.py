from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.views import generic 
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.urls import reverse_lazy
from django.views.generic import DetailView,CreateView
from .forms import SignUpForm,EditProfileForm,PasswordUpdateform,ProfilePageForm
from django.contrib.auth.views import PasswordChangeView
from blogapps.models import Profile
class MakeProfilePage(CreateView):
    model = Profile
    # form_class = ProfilePageForm
    fields = ['bio','inquiry','profilephoto','website_url','facebook_url','instagram_url','linkedin_url']
    # fields = '__all__'
    template_name = 'registration/userprofilecreation.html'
    def form_valid(self, form):
        
         return super().form_valid(form)
class ShowProfilePageView(DetailView):
    model = Profile 
    template_name = 'registration/user_profile.html'
    fields = ['user','bio','inquiry','profilephoto','website_url','facebook_url','instagram_url','linkedin_url']
    success_url = reverse_lazy('home')
    
    
    def get_context_data(self, *args, **kwargs):
    #   users= Profile.objects.all()
      context = super(ShowProfilePageView,self).get_context_data(*args,**kwargs)
      page_user = get_object_or_404(Profile,id = self.kwargs['pk'])
      context['page_user'] = page_user
      return context

class EditprofileView(generic.UpdateView):
    model = Profile
    template_name = 'registration/editprofilepage.html'
    fields = ['bio','inquiry','profilephoto','website_url','facebook_url','instagram_url','linkedin_url']
    success_url = reverse_lazy('home')

class PasswordChangeView(PasswordChangeView):
  form_class = PasswordUpdateform
  success_url = reverse_lazy('password_update')
def password_success(request):
        return render(request,'registration/password_success.html',{})

class UserRegisterView(generic.CreateView):
    form_class =SignUpForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')
   
# class UserRegisterView(generic.CreateView):
#     form_class = UserCreationForm
#     template_name = 'registration/registration.html'
#     success_url = reverse_lazy('login')

class UserUpdateView(generic.UpdateView):
    form_class= EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')
    def get_object(self):
        return self.request.user
    # print(get_object)


