import os
from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.http import QueryDict
from django.contrib.auth.decorators import login_required
import web
from .forms import CreateUserForm
from .models import Book, FeedBack
from .forms import AddBook
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
app_name = web
# Create your views here.

def firstpage(request):
    return render(request, 'firstpage.html')
def base(request):
    return render(request, 'base.html')
def home(request):
    BF = Book.objects.filter()
    return render(request, 'home.html', {'BF':BF})
#quản lý sách
def manage_book(request):
    BF = Book.objects.filter()
    return render(request, 'manage_book.html', {'BF':BF})
def chatroom(request):
    return render(request, 'chatroom.html')

#thêm sách 
def add_book(request):
    AB = AddBook
    return render(request, 'add_book.html',{'AB': AB})
#tải sách
def getFiles(request):
    form = AddBook(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, 'Tải sách thành công')
        return redirect('manage_book')
#hiện sách ở home
def get_book(request):
    BF = Book.objects.filter()
    return render(request, 'home.html', {'BF':BF})

#xóa sách
def delete(request, book_id):
    member = Book.objects.get(book_id=book_id)
    member.delete()
    messages.success(request, 'Xóa sách thành công')
    return redirect('manage_book')


def update_book(request, book_id):
    edit = Book.objects.get(book_id=book_id)

    if request.method == "POST":
        if len(request.FILES) !=0:
            if len(edit.cover_book) >=0:
                os.remove(edit.cover_book.path)
            edit.cover_book = request.FILES.get('cover_book')
            if len(edit.book) >=0:
                os.remove(edit.book.path)
            edit.book = request.FILES.get('book')
        edit.title = request.POST.get('title')
        edit.author = request.POST.get('author')
        edit.save()
        messages.success(request, "Chỉnh sửa sách thành công")
        return redirect('home')

    return render(request, 'update_book.html', {'edit':edit})
def search(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        keys = Book.objects.filter(book__contains = searched)
    return render(request, 'search.html', {"searched" : searched, "keys" : keys})
def manage_user(request):
    Mu = User.objects.filter()
    return render(request, 'manage_user.html', {'Mu':Mu})
def delete_user(request, username):
  user = User.objects.get(username=username)
  user.delete()
  messages.success(request, 'Xóa sách thành công')
  return redirect('manage_user')
def i4_user(request):
    return render(request, 'i4_user.html')
def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            if username == "admin":
                return redirect('home')
            else:
                return redirect('user_home')
        else: 
            messages.error(request, 'Đăng nhập không thành công. Vui lòng kiểm tra tên đăng nhập và mật khẩu.')

    context= {}
    return render(request, 'login.html', context)

def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
        else:
            messages.error(request, 'Mật khẩu không khớp')
    context = {'form':form}
    return render(request, 'register.html', context)


#user-interface
def user_home(request):
    BF = Book.objects.filter()
    return render(request, 'user_home.html', {'BF': BF})
def chatroom_user(request):
    return render(request, 'chatroom_user.html')
def user_search(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        keys = Book.objects.filter(book__contains = searched)
    return render(request, 'user_search.html', {"searched" : searched, "keys" : keys})

def add_feedback(request):
   return render(request,'add_feedback.html')

def Feedback(request):
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        feedback=request.POST["feedback"]
        obj=FeedBack(name=name, email=email, feedback=feedback)
        obj.save()
        return HttpResponse("<h2> Feedback hass bees submited </h2>")
        #return redirect('success')
    
    return render(request,'feedback.html')

def view_feedback(request):
    feedbacks=FeedBack.objects.all()
    return render(request,'view_feedback.html',{'feedbacks': feedbacks})




def favorites(request):
    BF = Book.objects.filter(is_favorite=True)
    return render(request, 'favorites.html', {'BF':BF})

def toggle_favorite(request, book_id):
    try:
        book = Book.objects.get(book_id=book_id)
        book.is_favorite = not book.is_favorite
        book.save()
        return JsonResponse({'is_favorite': book.is_favorite})
    except Book.DoesNotExist:
        return JsonResponse({'error': 'Book not found'}, status=404)
    
