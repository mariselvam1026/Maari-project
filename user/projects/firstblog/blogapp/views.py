from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.views import generic
from .models import post


# Create your views here.

class PostList(generic.ListView):
    queryset = post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blogapp/index.html'

class PostDetail(generic.DetailView):
    model = post
    template_name = 'blogapp/post_detail.html'


def register(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username=request.POST['username'])
                return render(request,'blogapp/register.html',{'error':'Username is already taken'})

            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('/')
        else:
            return render (request,'blogapp/register.html', {'error':'Password does not match'})
    else:
        return render(request,'blogapp/register.html')

def login(request):
    if request.method == "POST":
        user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('/')

        else:
            return render (request,'blogapp/login.html', {'error':'Username and Password does not match'})

    else:
        return render(request, 'blogapp/login.html')

def logout(request):
    if request.method == "POST":
        auth.login(request)
    return render('/')
    






    



