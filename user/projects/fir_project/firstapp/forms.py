from django import forms 
from django.forms.fields import CharField, EmailField,ImageField
from django.forms.widgets import  PasswordInput,EmailInput


from .models import Post,Comment

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        
        fields = '__all__'
        


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body')

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body')

class EmailPostForm(forms.Form):
    name = CharField(max_length=20)
    email = EmailField()
    to = EmailField()

    

# class PasswordResetForm(forms.PasswordResetForm):
#     email  = forms.EmailField(widget=forms.EmailInput(attrs={'class':"form-control"}))

# class PasswordResetConfirmForm(forms.SetPasswordForm):
#     new_password1 = forms.CharField(widget=PasswordInput(attrs={'class':'form-control'}), label='New password')
#     new_password2 = forms.CharField(widget=PasswordInput(attrs={'class':'form-control'}), label='Confirm new password')


        
