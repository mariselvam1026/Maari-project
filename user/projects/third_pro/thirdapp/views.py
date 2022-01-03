#from django.shortcuts import render
# Create your views here.
from django.db.models import fields
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.views import generic
from django.views.generic import DetailView
# from django.views.generic.edit import CreateView
from .forms import BlogPostForm
from django.shortcuts import render, get_object_or_404
from .forms import CommentForm,ReplyForm
from .models import Post,Comment



# from firstblog.blogapp.models import post

#from .blogapp.models import post



def register(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username=request.POST['username'])
                return render(request,'firstapp/register.html',{'error':'Username is already taken'})

            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('/')
        else:
            return render (request,'firstapp/register.html', {'error':'Password does not match'})
    else:
        return render(request,'firstapp/register.html')

def login(request):
    if request.method == "POST":
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('/')

        else:
            return render (request,'firstapp/login.html', {'error':'Username and Password does not match'})

    else:
        return render(request, 'firstapp/login.html')

def logout(request):
    if request.method == "POST":
        auth.login(request)
    return render('/')

def frontpage(request):
    posts=Post.objects.filter(status=1).order_by('-title')
    return render(request, 'firstapp/index.html', {'posts':posts})

# def edit(request):
#     posts=Post.objects.get('Content')
#     return render(request, 'firstapp/edit.html', {'posts':posts})

def new_post(request):
  
    if request.method == 'GET':
        form = BlogPostForm()


    else:
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            new_p = form.save()
            return redirect('frontpage')

   
    return render(request, 'firstapp/add.html', {'form': form})
    # elif request.method == 'POST':






# class Addpost(CreateView):
#     model = Post
#     template_name = 'firstapp/add.html'
#     fields = '__all__'





# class PostList(ListView):
#     template_name = 'firstapp/index.html'

#     def post(request):
#         post=Post.objects.filter(status=1).order_by('-title')
#         print("print:",post)
#         context = {
#             'post':post
#         }

#         print("aaaa:",context)
#         return render(request, 'firstapp/index.html',posts=context)
    # queryset = Post.objects.filter(status=1).order_by('-created_on')
    # posts=queryset
    # template_name = 'firstapp/index.html'


class PostDetail(DetailView):
    # print('ggg')
    model = Post
    template_name = 'firstapp/post_detail.html'

# class Addcomment(CreateView):
#     model = Comment
#     template_name = 'firstapp/comment.html'

#     fields = '__all__'


def add_comment(request, pk=None):
    print('slug',pk)
    print("request =",request)
    #template_name = 'firstapp/post_detail.html'
    post = get_object_or_404(Post, pk=pk)
    print('post:',post)
    comments = post.comments.filter(active=True)
    try:
        print('comments:',comments)
    except Exception as e:
        print("error=",e)

    new_comment = None
    print('hello')
    print("method =",request.method)
    if request.method == 'POST':
        print('hello')
        comment_form = CommentForm(request.POST)
        print("comment_form = ", comment_form)
        if comment_form.is_valid():
            try:
                new_comment = comment_form.save(commit=False)
                new_comment.post = post
                new_comment.save()
            except Exception as e:
                print("error = ",e)
            #return redirect('firstapp/post_detail.html', pk=post.pk)
            return redirect('add_comment', pk=post.pk)           
           
        
    else:
        print('hello')
        #template_name = 'firstapp/com.html'
        comment_form = CommentForm()
        print('Hiii')
        #return render(request, template_name , {'comment_form': comment_form, 'new_comment': new_comment})

    print('Ans:',comments)
    
    return render(request, 'firstapp/post_detail.html' , {'comments': comments,'post':post,'comment_form': comment_form,'new_comment': new_comment})


# def add_comment(self,request,post_pk,pk):
#     post=Post.objects.get(pk=post_pk)
#     parent_comment=Comment.objects.get(pk=pk)
#     form=CommentForm(request.POST)
#     if form.is_valid():
#         new_comment=form.save(commit=False)
#         new_comment.author=request.user
#         new_comment.post=post
#         new_comment.parent=parent_comment
#         new_comment.save()

#         return redirect('add_comment',pk=post_pk)

#     else:
#         comment_form = CommentForm()

#         return render(request, 'firstapp/post_detail.html' , {'comments': comments,'post':post,'comment_form': comment_form,'new_comment': new_comment})



def reply_comment(request,id,pk):
    print('pk',pk)
    print('Rammmm')
    print('aaaaa',request.POST)
    comment = get_object_or_404(Comment,pk=pk)
    #comment = Comment.objects.get(id=request.POST.get('comment_id'))

    print("method111 =", request.method)
    if request.method == 'POST':

        reply_form = ReplyForm(request.POST)
        print("reply",reply_form)

        if reply_form.is_valid():
            print("Hiiiiiiiiii")
            reply = reply_form.save(commit=False)
            reply.comment = comment
            #reply.author = request.user
           
            reply.save()
            print("Hlooooo")
            print('pk =',comment.pk, reply.post.pk)

            return redirect(f'/post/{comment.post.pk}/comment/{comment.pk}/reply')
            #return redirect('reply_comment',pk=comment.pk)
    else:
        reply_form = ReplyForm()
        print("Maariii")
    return render(request, 'firstapp/post_detail.html', {'reply_form':reply_form})



# def reply_comment(request,id, post):
#     post = get_object_or_404(Post, slug=post)
#     comments = post.comments.filter(active=True, parent__isnull=True)
#     if request.method == 'POST':
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#             parent_obj = None
#             try:
#                 parent_id = int(request.POST.get('parent_id'))
#             except:
#                 parent_id = None
#             if parent_id:
#                 parent_obj = Comment.objects.get(id=parent_id)
#                 if parent_obj:
#                     replay_comment = comment_form.save(commit=False)
#                     replay_comment.parent = parent_obj
#             new_comment = comment_form.save(commit=False)
#             new_comment.post = post
#             new_comment.save()
#     else:
#         comment_form = CommentForm()
#     return render(request, 'firstapp/postdetail.html',{'post': post, 'comments': comments,'comment_form': comment_form})
