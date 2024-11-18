from django import forms
from .models import Post,Category
#choices = [('coding','coding'),('dance','dance'),('music','music'),('badminton','badminton')]
choices = Category.objects.all().values_list('name','name')
# choice_list = []
# for item in choices:
#   choice_list.append(item)

class Postform(forms.ModelForm):
  class Meta:
    model = Post
    fields = ("title", 'title_tag', 'author', 'body','category','author_img','snippet')
    widgets = {
        'title':forms.TextInput(attrs={'class':'form-control'}),# we can find the query set here by using the placeholder= choices
        'title_tag':forms.TextInput(attrs={'class':'form-control'}),
        'auhtor':forms.Select(attrs={'class':'form-control',}),
        'body':forms.Textarea(attrs={'class':'form-control'}),
        'category':forms.Select(choices= choices,attrs={'class':'form-control','placeholder':choices}),
        'author_img':forms.FileInput(attrs={'class':'form-control'}),
        'snippet':forms.Textarea(attrs={'class':'form-control'}),
    }
class EditForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ("title", 'title_tag', 'author', 'body','author_img')
    widgets = {
        'title':forms.TextInput(attrs={'class':'form-control'}),
        'title_tag':forms.TextInput(attrs={'class':'form-control'}),
        'auhtor':forms.Select(attrs={'class':'form-control','placeholder':'username','id':'elder'}),
        'body':forms.Textarea(attrs={'class':'form-control'}),
         'author_img':forms.FileInput(attrs={'class':'form-control'}),

    }

class DeleteForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ("title", 'title_tag', 'author', 'body', 'author_img')
    widgets = {
        'title':forms.TextInput(attrs={'class':'form-control','placeholder':'this is the title placeholder stuff'}),
        'title_tag':forms.TextInput(attrs={'class':'form-control'}),
        'auhtor':forms.Select(attrs={'class':'form-control'}),
        'body':forms.Textarea(attrs={'class':'form-control'}),
         'author_img':forms.FileInput(attrs={'class':'form-control'}),
    }
