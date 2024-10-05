from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Member
from .models import *
from django.forms import inlineformset_factory
from .models import Member
from .models import Book
from django.contrib import messages
from .forms import MemberForm,BookForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect,render
from email.message import EmailMessage
import random
import smtplib



from django.contrib.auth.forms import UserCreationForm
# Create your views here.


#where pk is the primary - request,pk in parentheseis afer join TO CREATE A DYNAMIC URL - # customer =Customer.objects.all(id=pk)
# def join(request):
#
#     return render(request,"Auth/Login.html",{})

def pptc(request):
    return render(request, "Auth/Priv.html", {})
@login_required(login_url="Login")
def del1(request):
    if request.user.is_authenticated:
        global aaj #AAJ is the name of the user that is currently logged in
        aaj=request.user
        if True:
            a=int(request.POST.get("len1"))
            #print("_________________ssss_______")
            #print(aaj,a)
            aaj = str(aaj)
            count=1
            if True:
                for i in Book.objects.all():
                    #print(i.user,aaj,count,a)
                    #print(i.user==aaj and count==a)
                    #print(i.user==aaj and count==a)
                    if i.user==aaj and count==a:
                        i.delete()
                        #(Book.objects.filter(age=i.age,price=i.price,author=i.author,subject=i.subject,volume=i.volume,edition=i.edition,book_class=i.book_class).first()).delete

                        #print("aaaaat")
                        break
                    count=count+1

                return redirect("/book-list/")



    #return redirect("http://127.0.0.1:8000/book-list/")
    return redirect("/book-list/")

def join2(request):


    if not(request.user.is_authenticated):
        global form
        list_emails=[]
        #print("_____________________________________________")
        for i in Member.objects.all():
            #print(i)
            list_emails.append(i.email.lower())
        #print(list_emails)
        list_username=[]
        for i in Member.objects.all():
            #print(i)
            list_username.append(i.username)
        #print(list_emails)

        form = MemberForm(request.POST or None)

        params = {"form": form,"Error":""}

        print("CHECKBOX111")
        ab=request.POST.getlist('checks[]')
        print(ab)
        if form.is_valid() and len(ab)>0:

            if (form.cleaned_data['passwd'] == form.cleaned_data['passwd1']) and ((form.cleaned_data['email'].lower() not in list_emails)) and (str(form.cleaned_data['username']) not in list_username):
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login('aajbookotp@gmail.com', "lpyy ddeb yyae nhde")
                global otp
                otp=""

                for i in range(7):
                    a = str(random.randint(0, 9))
                    otp += a
                #print(otp)
                msg = EmailMessage()
                msg['Subject'] = "AAJBook.com OTP Verification"
                msg["From"] = "aajbookotp@gmail.com"
                msg["To"] = form.cleaned_data['email'].lower()
                #print("Email To:",form.cleaned_data['email'].lower())
                msg.set_content(f"Your Otp is :{otp}")
                server.send_message(msg)
                #print("EmailSent")
                # en=otp1(request)




                return redirect("otp")
                # form.save()

            elif not(form.cleaned_data['passwd'] == form.cleaned_data['passwd1']):
                return render(request, "Auth/Register.html", {"Error":"Both Passwords Don't Match!"})
            elif (form.cleaned_data['email'] in list_emails):
                return render(request, "Auth/Register.html", {"Error":"Email already has an account. Go to the Login Page or use a different email!"})
            elif (form.cleaned_data['username'] in list_username):
                return render(request, "Auth/Register.html", {"Error":"Username already exists. Select a new Username Please!"})

        else:
            #print("NOT VALID!!!")
            return render(request, "Auth/Register.html",params)
    return redirect("home")

def otp1(request):
    #print("NewFunc")

    if request.POST.get("otp") is not None:
        #print("Enter otp",request.POST.get("otp"))
        #print("Sent otp",otp)
        if request.POST.get("otp")==otp:
            form.save()
            user1 = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'],
                                            form.cleaned_data['passwd'])

            # At this point, user is a User object that has already been saved
            # to the database. You can continue to change its attributes
            # if you want to change other fields.
            user1.last_name = form.cleaned_data['lname']
            user1.first_name = form.cleaned_data['fname']
            user1.save()
            messages.success(request, "Account was created for" + form.cleaned_data['email'])
            return redirect("Login")

    else:

        return render(request,"Auth/RegisterNew.html")

aaj=None
def join(request):
    if not(request.user.is_authenticated):
        if request.method=="POST":
            email=request.POST.get("email")
            username=request.POST.get("username")
            passwd=request.POST.get("passwd")
            #print(email,passwd,username)
            user=None
            for i in Member.objects.all():
                if i.username==username and i.email==email and i.passwd==passwd:
                    global aaj
                    user=authenticate(request,username=i.username,email=i.email,password=i.passwd)
                    #print(user.username)
                    aaj=user.username



            if user is not None:
                #print("USER FOUND!")
                login(request,user)
                return redirect("home")
            else:
                pass
                #print(user,1111)

        return render(request,"Auth/Login.html",{"Error":"The username or password was wrong!"})
    return redirect("home")


def logout1(request):
    logout(request)
    return redirect("Login")
@login_required(login_url="Login")
def home(request):
    return render(request,"Auth/TempHome.html")





from django.shortcuts import render

from datetime import datetime
import asyncio

from typing import AsyncGenerator
from django.shortcuts import render, redirect
from django.http import HttpRequest, StreamingHttpResponse, HttpResponse
from . import models
import json
import random

# @login_required(login_url="Login")
# def lobby(request: HttpRequest) -> HttpResponse:
#
#     request.session['username'] = aaj
#
#     return redirect('chat')
#
# @login_required(login_url="Login")
# def chat(request: HttpRequest) -> HttpResponse:
#     return render(request, 'Auth/chat.html',{"user":aaj})
#
# @login_required(login_url="Login")
# def create_message(request: HttpRequest) -> HttpResponse:
#     content = request.POST.get("content")
#     #username=aaj
#     username =
#
#
#
#
#     # author, _ = models.Author.objects.get_or_create(name=a)
#
#     if content:
#         models.Message.objects.create(author=username, content=content)
#         return HttpResponse(status=201)
#     else:
#         return HttpResponse(status=200)
#
#
# async def stream_chat_messages(request: HttpRequest) -> StreamingHttpResponse:
#     """
#     Streams chat messages to the client as we create messages.
#     """
#     async def event_stream():
#         """
#         We use this function to send a continuous stream of data
#         to the connected clients.
#         """
#         async for message in get_existing_messages():
#             yield message
#
#         last_id = await get_last_message_id()
#
#         # Continuously check for new messages
#         while True:
#             new_messages = models.Message.objects.filter(id__gt=last_id).order_by('created_at').values(
#                 'id', 'author__name', 'content'
#             )
#             async for message in new_messages:
#                 yield f"data: {json.dumps(message)}\n\n"
#                 last_id = message['id']
#             await asyncio.sleep(0.1)  # Adjust sleep time as needed to reduce db queries.
#
#     async def get_existing_messages() -> AsyncGenerator:
#         messages = models.Message.objects.all().order_by('created_at').values(
#             'id', 'author__name', 'content'
#         )
#         async for message in messages:
#             yield f"data: {json.dumps(message)}\n\n"
#
#     async def get_last_message_id() -> int:
#         last_message = await models.Message.objects.all().alast()
#         return last_message.id if last_message else 0
#
#     return StreamingHttpResponse(event_stream(), content_type='text/event-stream')
#
#
#
#
#

#
#
from django.shortcuts import render

from datetime import datetime
import asyncio

from typing import AsyncGenerator
from django.shortcuts import render, redirect
from django.http import HttpRequest, StreamingHttpResponse, HttpResponse
from . import models
import json
import random

@login_required(login_url="Login")
def lobby(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':

        #print(aaj)
        request.session['username'] = aaj


        return redirect('chat')
    else:
        return render(request, 'Auth/lobby.html')


@login_required(login_url="Login")
def chat(request: HttpRequest) -> HttpResponse:
    if not request.session.get('username'):
        return redirect('lobby')
    return render(request, 'Auth/chat.html')


def create_message(request: HttpRequest) -> HttpResponse:
    content = request.POST.get("content")
    username = request.session.get("username")

    if not username:
        return HttpResponse(status=403)
    author, _ = models.Author.objects.get_or_create(name=username)

    if content:
        models.Message.objects.create(author=author, content=content)
        #print(content)
        #print("Message stored", author)
        return HttpResponse(status=201)
    else:
        return HttpResponse(status=200)


async def stream_chat_messages(request: HttpRequest) -> StreamingHttpResponse:
    """
    Streams chat messages to the client as we create messages.
    """
    async def event_stream():
        """
        We use this function to send a continuous stream of data
        to the connected clients.
        """
        async for message in get_existing_messages():
            yield message

        last_id = await get_last_message_id()

        # Continuously check for new messages
        while True:
            new_messages = models.Message.objects.filter(id__gt=last_id).order_by('created_at').values(
                'id', 'author__name', 'content'
            )
            async for message in new_messages:
                yield f"data: {json.dumps(message)}\n\n"
                last_id = message['id']
            await asyncio.sleep(0.3)  # Adjust sleep time as needed to reduce db queries.

    async def get_existing_messages() -> AsyncGenerator:
        messages = models.Message.objects.all().order_by('created_at').values(
            'id', 'author__name', 'content'
        )
        async for message in messages:
            yield f"data: {json.dumps(message)}\n\n"

    async def get_last_message_id() -> int:
        last_message = await models.Message.objects.all().alast()
        return last_message.id if last_message else 0

    return StreamingHttpResponse(event_stream(), content_type='text/event-stream')




#cd ./MainWebsite/
#python manage.py runserver


# from datetime import datetime
# import asyncio
#
# from typing import AsyncGenerator
# from django.shortcuts import render, redirect
# from django.http import HttpRequest, StreamingHttpResponse, HttpResponse
# from . import models
# import json
# import random
#
#
# def lobby(request: HttpRequest) -> HttpResponse:
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         if username:
#             request.session['username'] = username
#         else:
#             names = [
#                 "Horatio", "Benvolio", "Mercutio", "Lysander", "Demetrius", "Sebastian", "Orsino",
#                 "Malvolio", "Hero", "Bianca", "Gratiano", "Feste", "Antonio", "Lucius", "Puck", "Lucio",
#                 "Goneril", "Edgar", "Edmund", "Oswald"
#             ]
#             request.session['username'] = f"{random.choice(names)}-{hash(datetime.now().timestamp())}"
#
#         return redirect('chat')
#     else:
#         return render(request, 'Auth/lobby.html')
#
#
# def chat(request: HttpRequest) -> HttpResponse:
#     if not request.session.get('username'):
#         return redirect('lobby')
#     return render(request, 'Auth/chat.html')
#
#
# def create_message(request: HttpRequest) -> HttpResponse:
#     content = request.POST.get("content")
#     username = request.session.get("username")
#
#     if not username:
#         return HttpResponse(status=403)
#     author, _ = models.Author.objects.get_or_create(name=username)
#
#     if content:
#         models.Message.objects.create(author=author, content=content)
#         return HttpResponse(status=201)
#     else:
#         return HttpResponse(status=200)
#
#
# async def stream_chat_messages(request: HttpRequest) -> StreamingHttpResponse:
#     """
#     Streams chat messages to the client as we create messages.
#     """
#     async def event_stream():
#         """
#         We use this function to send a continuous stream of data
#         to the connected clients.
#         """
#         async for message in get_existing_messages():
#             yield message
#
#         last_id = await get_last_message_id()
#
#         # Continuously check for new messages
#         while True:
#             new_messages = models.Message.objects.filter(id__gt=last_id).order_by('created_at').values(
#                 'id', 'author__name', 'content'
#             )
#             async for message in new_messages:
#                 yield f"data: {json.dumps(message)}\n\n"
#                 last_id = message['id']
#             await asyncio.sleep(0.1)  # Adjust sleep time as needed to reduce db queries.
#
#     async def get_existing_messages() -> AsyncGenerator:
#         messages = models.Message.objects.all().order_by('created_at').values(
#             'id', 'author__name', 'content'
#         )
#         async for message in messages:
#             yield f"data: {json.dumps(message)}\n\n"
#
#     async def get_last_message_id() -> int:
#         last_message = await models.Message.objects.all().alast()
#         return last_message.id if last_message else 0
#
#     return StreamingHttpResponse(event_stream(), content_type='text/event-stream')


from django.shortcuts import render, redirect
from .forms import BookForm
from .models import Book
@login_required(login_url="Login")
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():

            obj = form.save(commit=False)
            obj.user = request.user

            obj.save()
            # form.cleaned_data["user"]=request.user
            # form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    user=request.user
    return render(request, 'Auth/book_form.html', {'form': form,"user":user})
@login_required(login_url="Login")
def book_list(request):
    books = Book.objects.all()
    #print("+++++++++++++++++++++++++++++++++++=")
    #print(aaj)
    return render(request, 'Auth/book_list.html', {'books': books})

