from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Chat, Message


@csrf_exempt
def create_chat(request):#1
    if request.method == 'POST':
        new_chat = Chat()
        new_chat.first_user_id = request.POST.get('first_user')
        new_chat.second_user_id = request.POST.get('second_user')
        new_chat.save()
        return JsonResponse({'new_chat':new_chat})
    return HttpResponse(status=405)


def chat_detail(request, chat_id):#2
    if request.method == 'GET':
        chat_object = get_object_or_404(Chat, id=chat_id)
        chat_info = [
                {
                'id':chat_id,
                'first_user':chat_object.first_user_id,
                'second_user':chat_object.second_user_id,
                'is_archive':chat_object.is_archive
            }
        ]
        return JsonResponse({'chats': chat_info })
    return HttpResponse(status=405)


def message_list(request, chat_id, chatuser_id):#3
    if request.method == 'GET':
        chat = get_object_or_404(Chat, id=chat_id)
        all_messages = chat.chat_message.filter(sent_from=chatuser_id).values()
        return JsonResponse({f'all messages from chat with chat_id={chat_id} and author with chatuser_id={chatuser_id}':list(all_messages)})
    return HttpResponse(status=405)


def edit_message(request, message_id):#4
    if request.method == 'POST':
        message = get_object_or_404(Message, id=message_id)
        message.text = request.POST.get('text')
        message.save()
        return JsonResponse({f'message with id {message_id}':'was edited'})
    return HttpResponse(status=405)


def delete_chat(request, chat_id):#5
    if request.method == 'DELETE':
        chat = get_object_or_404(Chat, id=chat_id)
        chat.delete()
        return JsonResponse({f'chat with id {chat_id}':'was deleted'})
    return HttpResponse(status=405)


def chat_page(request):
    if request.method == 'GET':
        return HttpResponse('<h1>It`s chat page</h1>')
    return HttpResponse(status=405)
