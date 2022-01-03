# from views import *
from django.contrib.auth.views import PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetDoneView
from django.urls import path
from firstapp.views import *
# from api import views


urlpatterns = [
    #path('', views.PostList.as_view(), name='home'),
    path('register/',register, name='register'),
    path('login/',login, name='login'),
    path('logout/',logout,name='logout'),
    #path('forgetpassword/',forgetpassword, name='forgetpassword'),
    path('password_reset/', password_reset, name="password_reset"),
    path('password_reset_done',PasswordResetDoneView.as_view(template_name='firstapp/password_reset_done.html'), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='firstapp/reset_complete.html'), name="password_reset_confirm"),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(template_name='firstapp/reset_confirm.html'), name="password_reset_complete"),
    path('changepassword/', changepassword , name='changepassword'),
    path('new_post/', new_post, name='new_post'), 
    path('', frontpage, name='home'),

   
    # path('update/<int:pk>',UpdatePostAPIView.as_view(),name="update_list"),
    path('delete/<int:id>',delete,name='delete'),
    path('post_list/',post_list , name='post_list'),
    path('update/<int:id>', update ,name = 'update'),
    path('signup/',signup,name='signup'),
    path('changepasswordapi/<int:id>', changepasswordapi,name='changepassword'),
    
    path('pageview/<int:id>', pageview, name= 'pageview'),
    #path('send_gmail/', send_gmail , name='send_gmail'),
    path('<int:post_id>/share/', send_gmail , name='send_gmail'),
    path('<slug:post>/', post_detail, name='post_detail'),
    

    
  
   
]