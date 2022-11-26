from django.urls import path
from chats import views

urlpatterns = [
    # path("message-list/<int:chat_id>", views.message_list),
    # path("chat-detail/<int:chat_id>", views.chat_detail),
    # path("chat-page", views.chat_page),
    # path("all-chats",  views.chat_list),
    path("chat/<int:pk>",  views.ChatInfo.as_view()),
    path("chat-list", views.ChatsList.as_view()),
    path("message-list/<int:chat_id>", views.MessageList.as_view()),
    path("message/<int:pk>", views.MessageInfo.as_view()),
    path("chat-members/<int:chat_id>", views.ChatMemberView.as_view()),
    path("chat-members/<int:chat_id>/<int:chat_user_id>", views.DeleteMemberView.as_view()),
]