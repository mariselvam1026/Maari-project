from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)

    content = RichTextField(blank=True,null = True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['created_on']

    # def __str__(self):
    #     return self.title


class Comment(models.Model): 
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80) 
    email = models.EmailField(max_length=80) 
    body = models.TextField() 
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True) 
    active = models.BooleanField(default=True) 
    parent = models.ForeignKey('self' ,on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    class Meta: 
        ordering = ('-created',) 

    def __str__(self): 
        return 'Comment by {} on {}'.format(self.name, self.post)


   
# class SubComment(models.Model):
    
#     replycomment=models.ForeignKey(Comment,on_delete=models.CASCADE,related_name='subcomments')
#     name = models.CharField(max_length=40) 
#     email = models.EmailField(max_length=40) 
#     body = models.TextField()
#     created = models.DateTimeField(auto_now_add=True) 
#     updated = models.DateTimeField(auto_now=True)
#     active = models.BooleanField(default=True) 
#     #parent = models.ForeignKey('self' ,on_delete=models.CASCADE, null=True, blank=True, related_name='reply')

#     class Meta: 
#         ordering = ('-created',) 

#     def __str__(self): 
#         return 'Comment by {} on {}'.format(self.name, self.replycomment)

   


