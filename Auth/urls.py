from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path("Login/",views.join,name="Login"),
    path("Logout/",views.logout1,name="logout"),
    path("Register/",views.join2,name="Register"),
    path("otp/",views.otp1,name="otp"),
    path("",views.home,name="home"),
    path('lobby/', views.lobby, name='lobby'),
    path('messages', views.chat, name='chat'), #From '' to 'messages'
    path('create-message/', views.create_message, name='create-message'),
    path('stream-chat-messages/', views.stream_chat_messages, name='stream-chat-messages'),
    path('add-book/', views.add_book, name='add_book'),
    path('book-list/', views.book_list, name='book_list'),
    path('delete_book/', views.del1, name='del1'),
path('privacypolicyandtermsandconditions/', views.pptc, name='pptc')
    # #path("join/<str:pk>",include()), TO CREATE A DYNAMIC URL
]


# urlpatterns = [
#     path('lobby/', views.lobby, name='lobby'),
#     path('', views.chat, name='chat'), #From '' to 'messages'
#     path('create-message/', views.create_message, name='create-message'),
#     path('stream-chat-messages/', views.stream_chat_messages, name='stream-chat-messages'),
# ]
from django.contrib import admin
from django.urls import path





