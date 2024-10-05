from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Member(models.Model):
    username = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=250)
    passwd = models.CharField(max_length=50)
    passwd1 = models.CharField(max_length=50)
    school = models.CharField(max_length=100)
    city = models.CharField(max_length=99)

    def __str__(self):
        return self.email

# class Books():
#     CustomerId=models.ForeignKey(Customer)
#     #all fields as per atharv
#
# class Order:
# CustomerId=models.ForeignKey(Customer,nll=)
# #BooksIdId=models.ForeignKey(Books)

from django.db import models

class Book(models.Model):
    user=models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    volume = models.IntegerField()
    edition = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    book_class = models.CharField(max_length=50)
    age = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.subject





class Author(models.Model):
    name = models.CharField(max_length=500)


class Message(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)