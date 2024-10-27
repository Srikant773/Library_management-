from django.db import models
from django.utils import timezone

class user_master(models.Model):
    student_name=models.CharField(max_length=200)
    regd_no=models.CharField(max_length=10)
    branch=models.CharField(max_length=30)
    year=models.CharField(max_length=80)
    section=models.CharField(max_length=30)
    image=models.ImageField(upload_to='images/')
    mobile=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    password=models.CharField(max_length=30)
    address=models.TextField(max_length=100)
    def __str__(self):
        return self.regd_no  #+  self.student_name

class college_master(models.Model):
    admin_name=models.CharField(max_length=30)
    email=models.CharField(max_length=20)
    password=models.CharField(max_length=40)
    mobile=models.CharField(max_length=10)
    def __str__(self):
        return self.admin_name

class add_book(models.Model):
    book_name=models.CharField(max_length=40)
    book_no=models.CharField(max_length=30)
    def __str__(self):
        return self.book_name

class book_issuse(models.Model):
    book_name=models.ForeignKey(add_book,on_delete=models.CASCADE)
    regd_no=models.ForeignKey(user_master,on_delete=models.CASCADE)
    date=models.DateField()    
    #(default=timezone.now)
# Create your models here.
