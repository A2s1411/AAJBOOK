from django import forms
from .models import Member
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import get_user_model

from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["user",'subject', 'volume', 'edition', 'author', 'book_class', 'age', 'price']



class MemberForm(forms.ModelForm):
    class Meta:
        model=Member
        # fields=['fname','lname',"email",'passwd','school','city']
        fields = ['username','fname', 'lname', "email", 'passwd','passwd1', 'school', 'city']
        # fields="__all__"
#
# class MemberForm(UserCreationForm):
#     email=forms.EmailField(help_text="A Valid Email Address Please",required=True)
#     # city = forms.CharField(help_text="Please Enter Your City",required=True)
#     # school = forms.CharField(help_text="Please Enter Your School", required=True)
#     class Meta:
#         model=Member
#         # fields=['fname','lname',"email",'passwd','school','city']
#         fields=['first_name','last_name',"username",'email','password1','password2']
#
#         # fields="__all__"
#
#     def save(self,commit=True):
#         user=super(MemberForm,self).save(commit=False)
#         user.email=self.cleaned_data['email']
#         if commit:
#             user.save()
#         return user