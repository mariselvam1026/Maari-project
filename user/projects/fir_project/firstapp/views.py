#from django.shortcuts import render
# Create your views here.
import json
import django
from django.db.models import fields
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.views import generic
# from django.views.generic import DetailView
# from django.views.generic import TemplateView

from .forms import BlogPostForm, ReplyForm, CommentForm
from .models import Post, Comment
from django.http import HttpResponseRedirect, request
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm
from django.contrib import messages
from django.contrib.auth.views import PasswordResetView
from django.shortcuts import get_object_or_404
from django.contrib.auth import views
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.conf import settings
# from django.contrib.auth.views import password_reset
# from rest_framework import generics
from .serializers import PostSerializer
from rest_framework.generics import ListAPIView
# from rest_framework.generics import CreateAPIView
# from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password

@csrf_exempt 
def post_list(request):
    if request.method == 'GET':
        # MAX_OBJECTS = 20
        data =Post.objects.values()
        #data =list(Post.objects.values())
        print("queryyy",data)
        # for text in data:
        #     print("fffff",text.id)
        dataa = {"result":list(data.values("id","title","slug","content"))}
        return JsonResponse(dataa)   
        # return JsonResponse(data , safe=False)

    elif request.method == 'POST':
        obj = JSONParser().parse(request)
        obj1 = request.data
        print("kkkk",obj)
        print("objjjjj",obj['title'])
        print("objjjjdddddj",obj['author_id'])
        print("sluggg",obj['slug'])
        print("status",obj['status'])
        user = User.objects.get(id=obj['author_id']) 
        print("user",user)
        data = Post.objects.create(title=obj['title'],slug=obj['slug'],author=user,content=obj['content'],status=obj['status'])
        print("DATAA : ",data)
        data.save()
        dataa = {"result":list(data.values("status","title","slug","content"))}
        print("aaaaaa",dataa)
        return JsonResponse(dataa)

    

@csrf_exempt 
def delete(request,id):
    print("hloooo")
    if request.method == 'DELETE':
        print("Hiiiii")
        post = Post.objects.get(id=id)  
        print("Post",post)
        post.delete()
        return JsonResponse("Deleted")

@csrf_exempt 
def update(request,id):
    if request.method == 'PUT':
        obj = JSONParser().parse(request)
        print("kkkk",obj)
        print("Titleee",obj['title'])
        print("IDDD",obj['author_id'])
        user = User.objects.get(id=obj['author_id']) 
        print("user",user)
        data = Post.objects.get(pk=id)
        print("aaa",data)
        data.title =obj['title']
        data.slug = obj['slug']
        data.save()
        dataa = {"results":{    
        }
        }
        print("aaaaaa",dataa)
        return JsonResponse(dataa)    

@csrf_exempt 
def signup(request):
    if request.method == 'POST':
        obj = JSONParser().parse(request)
        print(obj)
        ass = obj['password']
        password= make_password(ass)
        user = User.objects.values()
        print("USER",user)
        user = User.objects.create(username=obj['username'],email=obj['email'],password=password)
        print("Zz",user)
        user.save()
        dataa = {
            "result":list(user.values("username","email","password"))   
        }
        print(make_password('1111'))
        print(make_password('hlooo'))
        return JsonResponse(dataa)

@csrf_exempt 
def changepasswordapi(request,id):
    if request.method == 'PUT':
        obj = JSONParser().parse(request)
        print("kkkk",obj)
        print("username",obj['username'])
        print("password",obj['password'])
        # user = User.objects.get(id) 
        # print("user",user)
        data = User.objects.get(pk=id)
        print("aaa",data)
        ass = obj['password']
        password= make_password(ass)
        data.username =obj['username']
        data.password = password
        data.email = obj['email']
        data.save()
        dataa = {"results":{    
        }
        }
        print("aaaaaa",dataa)
        return JsonResponse(dataa)  

# class ListPostAPIView(ListAPIView):
   
#     queryset = Post.objects.all()
#     print("dara",queryset)
#     serializer_class = PostSerializer

# class UpdatePostAPIView(UpdateAPIView):
   
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
   



def password_reset(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            
            data = form.cleaned_data['email']
            print("dataa",data)
            
            user_email = User.objects.filter(Q(email=data))
            print("emailllll",user_email)
           
            if user_email.exists():
                try:
                    print("hlooo")
                    for user in user_email:
                        print(user)
                        subject = "Password Reset Requested"
                        email_template_name = "firstapp/password.txt"
                        detail = {
                            "email": user.email,
                            'domain': '127.0.0.1:8000',
                            'site_name': 'Website',
                            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                            "user": user,
                            'token': default_token_generator.make_token(user),
                            'protocol': 'http',
                        }
                        print("MAARII")
                        print("detail",detail)
                        email = render_to_string(email_template_name, detail)
                        try:
                            send_mail(subject, email, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)
                        except Exception as e:
                            print(str(e))
                            return HttpResponse('Invalid header found.')
                        return redirect("password_reset_done")
                except Exception as e:
                    print('errorrrr', e)
     
                    try:
                        send_mail(subject, email, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect("password_reset_done")

    form = PasswordResetForm()
    return render(request=request, template_name="firstapp/password_reset.html", context={"form": form})


def register(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username=request.POST['username'])
                return render(request, 'firstapp/register.html', {'error': 'Username is already taken'})

            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('/')
        else:
            return render(request, 'firstapp/register.html', {'error': 'Password does not match'})
    else:
        return render(request, 'firstapp/register.html')



def login(request):
    if request.method == "POST":
        user = auth.authenticate(
            username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            return render(request, 'firstapp/login.html', {'error': 'Username and Password does not match'})

    else:
        return render(request, 'firstapp/login.html')


def logout(request):
    if request.method == "POST":
        auth.login(request)
    return render('/')


# class PasswordResetView(PasswordResetView):
#     template_name = 'firstapp/password_reset.html'
#     form_class = PasswordResetForm
#     email_template_name = 'firstapp/password_email_reset.html'


# def forgetpassword(request):
#     if request.method == 'POST':
#         return password_reset(request, from_email=request.POST.get('email'))
#     else:
#         return render(request, 'firstapp/forgot_password.html')


def changepassword(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            # update the session after password change
            auth.update_session_auth_hash(request, form.user)
            messages.success(request, 'change password')

            return redirect('/')
        else:
            return redirect('changepassword')
    else:
        form = PasswordChangeForm(user=request.user)

        return render(request, 'firstapp/changepass.html', {'form': form})


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
            return redirect('/')

    return render(request, 'firstapp/add.html', {'form': form})


def post_detail(request, post):
    post = get_object_or_404(Post, slug=post)
    comments = post.comments.filter(active=True, parent__isnull=True)
    print("posttt", post)
    print("commentsss", comments)
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            parent_obj = None
            # child_obj=None
            try:
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None
            if parent_id:
                parent_obj = Comment.objects.get(id=parent_id)
                if parent_obj:
                    replay_comment = comment_form.save(commit=False)
                    replay_comment.parent = parent_obj

            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()

            print('comment_form', comment_form)
            comment_form = CommentForm()

            reply_form = ReplyForm()
            return render(request, 'firstapp/post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form, 'reply_form': reply_form})

    else:
        comment_form = CommentForm()
        reply_form = ReplyForm()

    return render(request, 'firstapp/post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form, 'reply_form': reply_form})


# def post_data(request, post):
# 	# post = get_object_or_404(Post, slug=post)
# 	# comments = post.comments.filter(active=True)
# 	if request.method == 'POST':
# 		reply_form = ReplyForm(data=request.POST)
# 		if reply_form.is_valid():
# 			new_comment = reply_form.save(commit=False)
# 			new_comment.post = post
# 			new_comment.save()
# 	else:
# 		reply_form = ReplyForm()

# 	return render(request,'firstapp/post_details.html',{'reply_form': reply_form})


def send_gmail(request, post_id):
    posts = get_object_or_404(Post, id=post_id)
    #posts = Post.objects.filter(status=1).order_by('-title')

    print("posts-", posts)
    print('id-', post_id)
    print("Hloooooo", request)
    if request.method == "POST":
        print("Hiiiiiiiiiii")
        print('request', request)
        to = request.POST.get('to')
        name = request.POST.get('name')
        print("name", name)

        message = request.POST.get('message')
        print(name, message, to)
        print("Hiiiiii")
        try:
            send_mail(
                name,
                message,
                'maariselvams1026@gmail.com',
                [to],
                fail_silently=False,
            )
        except Exception as e:
            print('errorrrr', e)

        return render(request, 'firstapp/mailpost.html', {'posts': posts})

    else:
        return render(request, 'firstapp/mailpost.html', {'posts': posts})


def frontpage(request):
    posts = Post.objects.filter(status=1).order_by('-title')
    return render(request, 'firstapp/index.html', {'posts': posts})


def pageview(request, id):

    post = get_object_or_404(Post, id=id)
    comments = post.comments.filter(active=True)

    comment_form = CommentForm()

    print("postttzzzzz", post)
    print("commentssszzzzz", comments)
    return render(request, 'firstapp/Twitt.html', {'post': post, 'comments': comments, 'comment_form': comment_form})
    # parent_id=request.POST.get("parent_id","")
