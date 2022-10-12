from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

def chat_list(request):
    if request.method == 'GET':
        chats = [
            {'id':1, 'title':'Family'},
            {'id': 2, 'title': 'Job'},
            {'id': 3, 'title': 'Classmates'},
        ]
        return JsonResponse({'chats':chats})
    return HttpResponse(status=405)


def chat_page(request):
    if request.method == 'GET':
        return HttpResponse('<h1>It`s chat page</h1>')
    return HttpResponse(status=405)

@csrf_exempt
def create_chat(request):
    if request.method == 'POST':
        return JsonResponse({'new_chat':'chat created'})
    return HttpResponse(status=405)
