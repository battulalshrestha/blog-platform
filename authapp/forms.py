from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from blogapps.models import Profile
class ProfilePageForm(forms.ModelForm):
  class Meta:
    model=Profile
    fields = ('bio','inquiry','profilephoto','website_url','facebook_url','instagram_url','linkedin_url')
    widgets = {
        'bio':forms.Textarea(attrs={'class':'form-control'}),# we can find the query set here by using the placeholder= choices
        'inquiry':forms.Textarea(attrs={'class':'form-control'}),
        # 'profilephoto':forms.Select(attrs={'class':'form-control',}),
        'website_url':forms.TextInput(attrs={'class':'form-control'}),
        'facebook_url':forms.TextInput(attrs={'class':'form-control'}),
        'instagram_url':forms.TextInput(attrs={'class':'form-control'}),
        'linkedin_url':forms.TextInput(attrs={'class':'form-control'}),
    }

class SignUpForm(UserCreationForm):
    # this widget makes the frontend part of reg large text area
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=60,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    photo_verification = forms.ImageField()
    class Meta:
        model = User
        # username,password1,password2 are already in django form --> in the forms of usename,password,confirm password
        fields = ('username','first_name','last_name','email','photo_verification','password1','password2')
    def __init__(self, *args, **kwargs):
        super(SignUpForm,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

class EditProfileForm(UserChangeForm):
    # this widget makes the frontend part of reg large text area
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=60,widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_login = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    is_superuser = forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    is_staff = forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    is_active =forms.CharField(max_length=100,widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    date_joined = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))



    photo_verification = forms.ImageField()
    class Meta:
        model = User
        # username,password1,password2 are already in django form --> in the forms of usename,password,confirm password
        fields = ('username','first_name','last_name','email','photo_verification','password','last_login','is_superuser','is_staff','is_active','date_joined')


class PasswordUpdateform(PasswordChangeForm):
    # this widget makes the frontend part of reg large text area
    old_password= forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1 = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2 = forms.CharField(max_length = 100,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        # username,password1,password2 are already in django form --> in the forms of usename,password,confirm password
        fields = ('old_password','new_password1','new_password2')