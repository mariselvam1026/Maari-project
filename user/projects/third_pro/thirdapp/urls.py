# from views import *
from django.urls import path
from firstapp.views import *

urlpatterns = [
    #path('', views.PostList.as_view(), name='home'),
    path('register/',register, name='register'),
    path('login/',login, name='login'),
    path('logout/',logout,name='logout'),
    # path('edit/',edit,name='edit'),
    path('new_post/', new_post, name='new_post'),
    path('', frontpage, name='home'),
  
    path('post/<int:pk>/comment', add_comment , name ='add_comment'),
    path('post/<int:id>/comment/<int:pk>/reply', reply_comment, name='reply_comment'),
    #path('post/<int:pk>/reply/',reply_comment,name='reply_comment'),
    
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
  
    
    
]