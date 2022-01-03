from django import forms

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


        
