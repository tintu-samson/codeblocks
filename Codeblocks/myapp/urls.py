from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('room/<str:pk>/',views.room,name='room'),
    path('create-room',views.createRoom,name='create-room'),
    path('update-room/<str:pk>',views.updateRoom,name='update-room'),
    path('delete-room/<str:pk>',views.deleteRoom,name='delete-room'),
     path('delete-message/<str:pk>/',views.deleteMessage,name='delete-message'),
    
    
    path('signup',views.signup,name='signup'),
    path('login',views.login_user,name='login'),
    path('logout',views.logout_user,name='logout'),
    
]