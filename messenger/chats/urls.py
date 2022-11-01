from django.urls import path
from chats import views

urlpatterns = [
    path("message-list/<int:chat_id>", views.message_list),
    path("chat-detail/<int:chat_id>", views.chat_detail),
    path("chat-page", views.chat_page),
    path("create-chat", views.create_chat),
    path("all-chats",  views.chat_list)
]