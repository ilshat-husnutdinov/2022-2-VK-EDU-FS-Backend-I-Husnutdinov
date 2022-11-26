from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from chats.serializers import ChatSerializer, MessageSerializer, ChatMemberSerializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListCreateAPIView, RetrieveDestroyAPIView
from django.db.models import Q
from .models import Chat, Message, ChatMember


class ChatInfo(RetrieveUpdateDestroyAPIView): # 2, 5, 13 (отредачить, удалить, получить чат по id)
    serializer_class = ChatSerializer

    def get_object(self):
        chat_id = self.kwargs['pk']
        return get_object_or_404(Chat, id=chat_id)


class ChatsList(ListCreateAPIView): # 1, 10 (Получить список чатов и создать чат)
    serializer_class = ChatSerializer
    queryset = Chat.objects.all()


class MessageInfo(RetrieveUpdateDestroyAPIView): # 7,8,9 (отредактировать, пометить прочитанным и удалить сообщение по его id)
    serializer_class = MessageSerializer

    def get_object(self):
        message_id = self.kwargs['pk']
        return get_object_or_404(Message, id=message_id)


class MessageList(ListCreateAPIView):# 6, 11 (получить список сообщений по id чата)
    serializer_class = MessageSerializer

    def get_queryset(self):
        chat_id = self.kwargs['chat_id']
        chat = get_object_or_404(Chat, id=chat_id)
        return chat.chat_message.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        chat_id = self.kwargs['chat_id']

        chat, sent_from = int(request.data['chat']), int(request.data['sent_from'])
        if chat_id != chat:
            return Response({'error':'you cant send message to other chat'}, status=409)
        if ChatMember.objects.get(pk=sent_from) not in ChatMember.objects.filter(chat=chat_id):
            return Response({'error':'user not in this chat'}, status=409)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ChatMemberView(ListCreateAPIView): #3 Добавить участника в чат по id чата и id человека
    serializer_class = ChatMemberSerializer

    def get_queryset(self):
        chat_id = self.kwargs['chat_id']
        return ChatMember.objects.filter(chat=chat_id)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        chat_id = self.kwargs['chat_id']
        chat = get_object_or_404(Chat, id=chat_id)
        chat_members = chat.chat_chatmember.values_list('chat_user', flat=True)

        request_chat_id = int(request.data['chat'])
        request_chat_user_id = int(request.data['chat_user'])
        if chat_id != request_chat_id:
            return Response({'error':'you cant add user to other chat'}, status=409)
        if request_chat_user_id in chat_members:
            return Response({'error':'the user is already in the chat'}, status=409)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class DeleteMemberView(RetrieveDestroyAPIView): #4 Удалить участника из чата по id чата и id человека
    serializer_class = ChatMemberSerializer

    def get_object(self):
        chat_id = self.kwargs['chat_id']
        chat_user_id = self.kwargs['chat_user_id']
        member = get_object_or_404(ChatMember, Q(chat=chat_id) & Q(chat_user=chat_user_id))
        return member








# class DeleteUser(RetrieveDestroyAPIView): #4 Удалить участника из чата по id чата и id человека
#     serializer_class = DeleteUserChatSerializer


#     def get_object(self):
#         queryset = ChatMember.

#     def get_queryset(self):
#         chat_id = self.kwargs['pk']
#         return Chat.objects.filter(id=chat_id)

# @require_http_methods(["POST"])
# def create_chat(request):#1
#     new_chat = Chat.objects.create(**request.POST)
#     new_chat_info = [{
#         'id':new_chat.pk,
#         'description':new_chat.description,
#         'title':new_chat.title,
#         'is_archive':new_chat.is_archive,
#         'created_ad':new_chat.creation_time
#     }]
#     return JsonResponse({'new_chat':new_chat_info}, status=201)


# @require_http_methods(["PATCH"])
# def edit_chat(request, chat_id):#2
#     chat = get_object_or_404(Chat, id=chat_id)
#     data = QueryDict(request.body)
#     chat.description = data.get('description')
#     chat.title = data.get('title')
#     chat.save(update_fields=['description','title'])
#     chat_info = [{
#         'id':chat.pk,
#         'description':chat.description,
#         'title':chat.title,
#     }]
#     return JsonResponse({f'edited fields for chat with id {chat_id}':chat_info})


# @require_http_methods(["PATCH"])
# def add_user(request, user_id, chat_id):#3
#     chat = get_object_or_404(Chat, id=chat_id)
#     user = get_object_or_404(AppUser, id=user_id)
#     if user in chat.users.all():
#         return JsonResponse(
#             {f'user with id {user_id}':f'already added before in chat with id {chat_id}'},
#             status=409
#         )
#     chat.users.add(user)
#     return JsonResponse({f'user with id {user_id}':f'added in chat with id {chat_id}'})


# @require_http_methods(["DELETE"])
# def delete_user(request, user_id, chat_id):#4
#     chat = get_object_or_404(Chat, id=chat_id)
#     user = get_object_or_404(AppUser, id=user_id)
#     if user not in chat.users.all():
#         return JsonResponse(
#             {f'user with id {user_id}':f'does not exist in chat with id {chat_id}'},
#             status=409
#         )
#     chat.users.remove(user)
#     return JsonResponse({f'user with id {user_id}':f'was deleted from chat with id {chat_id}'})


# @require_http_methods(["DELETE"])
# def delete_chat(request, chat_id):#5
#     chat = get_object_or_404(Chat, id=chat_id)
#     chat.delete()
#     return JsonResponse({f'chat with id {chat_id}':'was deleted'})


# @require_http_methods(["POST"])
# def send_message(request, chat_id, from_id, to_id):#6
#     chat = get_object_or_404(Chat, id=chat_id)
#     sent_from = get_object_or_404(AppUser, id=from_id)
#     sent_to = get_object_or_404(AppUser, id=to_id)
#     text = request.POST.get('text')
#     chat.chat_message.create(
#         sent_from=sent_from,
#         sent_to=sent_to,
#         text=text
#     )
#     new_msg_id = chat.chat_message.last().id
#     return JsonResponse(
#         {f'new message with id {new_msg_id} in chat with id {chat_id}':'was created'},
#         status=201
#     )


# @require_http_methods(["PATCH"])
# def edit_message(request, message_id):#7
#     message = get_object_or_404(Message, id=message_id)
#     data = QueryDict(request.body)
#     message.text = data.get('text')
#     message.save()
#     return JsonResponse({f'message with id {message_id}':'was edited'})


# @require_http_methods(["PATCH"])
# def read_message(request, message_id):#8
#     message = get_object_or_404(Message, id=message_id)
#     message.is_read = True
#     message.save()
#     return JsonResponse({f'message with id {message_id}':'was read'})


# @require_http_methods(["DELETE"])
# def delete_message(request, message_id):#9
#     message = get_object_or_404(Message, id=message_id)
#     message.delete()
#     return JsonResponse({f'message with id {message_id}':'was deleted'})


# @require_http_methods(["GET"])
# def chat_list(request):#10
#     all_chats = Chat.objects.all().values()
#     return JsonResponse({'all chats':list(all_chats)})


# @require_http_methods(["GET"])
# def message_list(request, chat_id):#11
#     chat = get_object_or_404(Chat, id=chat_id)
#     all_messages = chat.chat_message.values()
#     return JsonResponse({f'all messages from chat with chat_id={chat_id}':list(all_messages)})


# @require_http_methods(["GET"])
# def chat_detail(request, chat_id):#13
#     chat = get_object_or_404(Chat, id=chat_id)
#     chat_info = {
#             'id':chat_id,
#             'description':chat.description,
#             'title':chat.title,
#             'is_archive':chat.is_archive,
#             'created_at':chat.creation_time,
#             'users': [user.gen_info() for user in chat.users.all()],
#         }
#     return JsonResponse({'chats': chat_info })





# @require_http_methods(["GET"])
# def chat_page(request):
#     return HttpResponse('<h1>It`s chat page</h1>')

