from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your models here.


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'last_name', 'first_name' , 'password1', 'password2']

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    book = models.FileField(upload_to='files',null=True)
    cover_book = models.ImageField(upload_to='images', null=True)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}, {self.author}, {self.date}, {self.book}, {self.cover_book}"
    
    
class FeedBack(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


