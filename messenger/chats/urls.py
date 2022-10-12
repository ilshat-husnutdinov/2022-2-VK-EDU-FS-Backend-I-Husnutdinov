from django.urls import path
from . import views

urlpatterns = [
    path("chat-list", views.chat_list),
    path("chat-page", views.chat_page),
    path("create-chat", views.create_chat),
]