from django.http import JsonResponse, HttpResponse
from .models import ChatUser
from django.shortcuts import get_object_or_404


def all_users(request):
    if request.method == 'GET':
        users = ChatUser.objects.select_related()
        users_info = [
            {
                'id':user.id,
                'username':user.username,
                'first-name':user.first_name,
                'gender':user.gender,
            }
            for user in users
        ]
        return JsonResponse({'users':users_info})
    return HttpResponse(status=405)


def get_user(request, user_id):#12
    if request.method == 'GET':
        user = ChatUser.objects.filter(id=user_id).values()
        if len(user) == 0:
            return JsonResponse({'user':'does not exist'}, status=404)
        return JsonResponse({'user':list(user)})
    return HttpResponse(status=405)
# Create your views here.

