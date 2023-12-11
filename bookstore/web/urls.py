import statistics
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path

from bookstore import settings
from . import views
urlpatterns = [
    path('', views.firstpage),
    path('base/', views.base),
    path('home/', views.home, name='home'),
    path('user_home/', views.user_home, name='user_home'),
    path('user_home/chatroom_user', views.chatroom_user, name='chatroom_user'),
    path('user_home/user_search/', views.user_search, name='user_search'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.register, name='register'),
    path('home/manage_book/', views.manage_book, name='manage_book'),
    path('home/manage_book/update_book/<int:book_id>/', views.update_book, name='update_book'),
    path('manage_user/', views.manage_user, name='manage_user'),
    path('manage_user/delete_user/<str:username>', views.delete_user, name='delete_user'),
    path('manage_book/add_book.html', views.add_book, name='add_book'),
    path('home/manage_book/delete/<int:book_id>', views.delete, name='delete'),
    path('home/i4_user/', views.i4_user, name='i4_user'),
    path('home/search/', views.search, name='search'),
    path('chatroom/', views.chatroom, name='chatroom'),
    path('getFiles/', views.getFiles, name='getFiles'),
    path('', LogoutView.as_view(), name='logout'),
    path('feedback/', views.add_feedback, name='add_feedback'),
    path('feedback/feedback1/',views.Feedback, name='feedback'),
    path('view_feedback/', views.view_feedback, name='view_feedback'),
    path('favorites/', views.favorites, name='favorites'),
    path('toggle_favorite/<int:book_id>/', views.toggle_favorite, name='toggle_favorite'),
]


