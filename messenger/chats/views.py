from django.http import JsonResponse, HttpResponse, QueryDict
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from users.models import ChatUser
from .models import Chat, Message


@require_http_methods(["POST"])
def create_chat(request):#1
    new_chat = Chat.objects.create(**request.POST)
    new_chat_info = [{
        'id':new_chat.pk,
        'description':new_chat.description,
        'title':new_chat.title,
        'is_archive':new_chat.is_archive,
        'created_ad':new_chat.creation_time
    }]
    return JsonResponse({'new_chat':new_chat_info}, status=201)


@require_http_methods(["PATCH"])
def edit_chat(request, chat_id):#2
    chat = get_object_or_404(Chat, id=chat_id)
    data = QueryDict(request.body)
    chat.description = data.get('description')
    chat.title = data.get('title')
    chat.save(update_fields=['description','title'])
    chat_info = [{
        'id':chat.pk,
        'description':chat.description,
        'title':chat.title,
    }]
    return JsonResponse({f'edited fields for chat with id {chat_id}':chat_info})


@require_http_methods(["PATCH"])
def add_user(request, user_id, chat_id):#3
    chat = get_object_or_404(Chat, id=chat_id)
    user = get_object_or_404(ChatUser, id=user_id)
    if user in chat.users.all():
        return JsonResponse(
            {f'user with id {user_id}':f'already added before in chat with id {chat_id}'},
            status=409
        )
    chat.users.add(user)
    return JsonResponse({f'user with id {user_id}':f'added in chat with id {chat_id}'})


@require_http_methods(["DELETE"])
def delete_user(request, user_id, chat_id):#4
    chat = get_object_or_404(Chat, id=chat_id)
    user = get_object_or_404(ChatUser, id=user_id)
    if user not in chat.users.all():
        return JsonResponse(
            {f'user with id {user_id}':f'does not exist in chat with id {chat_id}'},
            status=409
        )
    chat.users.remove(user)
    return JsonResponse({f'user with id {user_id}':f'was deleted from chat with id {chat_id}'})


@require_http_methods(["DELETE"])
def delete_chat(request, chat_id):#5
    chat = get_object_or_404(Chat, id=chat_id)
    chat.delete()
    return JsonResponse({f'chat with id {chat_id}':'was deleted'})


@require_http_methods(["POST"])
def send_message(request, chat_id, from_id, to_id):#6
    chat = get_object_or_404(Chat, id=chat_id)
    sent_from = get_object_or_404(ChatUser, id=from_id)
    sent_to = get_object_or_404(ChatUser, id=to_id)
    text = request.POST.get('text')
    chat.chat_message.create(
        sent_from=sent_from,
        sent_to=sent_to,
        text=text
    )
    new_msg_id = chat.chat_message.last().id
    return JsonResponse(
        {f'new message with id {new_msg_id} in chat with id {chat_id}':'was created'},
        status=201
    )


@require_http_methods(["PATCH"])
def edit_message(request, message_id):#7
    message = get_object_or_404(Message, id=message_id)
    data = QueryDict(request.body)
    message.text = data.get('text')
    message.save()
    return JsonResponse({f'message with id {message_id}':'was edited'})


@require_http_methods(["PATCH"])
def read_message(request, message_id):#8
    message = get_object_or_404(Message, id=message_id)
    message.is_read = True
    message.save()
    return JsonResponse({f'message with id {message_id}':'was read'})


@require_http_methods(["DELETE"])
def delete_message(request, message_id):#9
    message = get_object_or_404(Message, id=message_id)
    message.delete()
    return JsonResponse({f'message with id {message_id}':'was deleted'})


@require_http_methods(["GET"])
def chat_list(request):#10
    all_chats = Chat.objects.all().values()
    return JsonResponse({'all chats':list(all_chats)})


@require_http_methods(["GET"])
def message_list(request, chat_id):#11
    chat = get_object_or_404(Chat, id=chat_id)
    all_messages = chat.chat_message.values()
    return JsonResponse({f'all messages from chat with chat_id={chat_id}':list(all_messages)})


@require_http_methods(["GET"])
def chat_detail(request, chat_id):#13
    chat = get_object_or_404(Chat, id=chat_id)
    chat_info = {
            'id':chat_id,
            'description':chat.description,
            'title':chat.title,
            'is_archive':chat.is_archive,
            'created_at':chat.creation_time,
            'users': [user.gen_info() for user in chat.users.all()],
        }
    return JsonResponse({'chats': chat_info })





@require_http_methods(["GET"])
def chat_page(request):
    return HttpResponse('<h1>It`s chat page</h1>')

