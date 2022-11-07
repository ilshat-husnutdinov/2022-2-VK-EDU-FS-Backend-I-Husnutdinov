from django.http import JsonResponse, HttpResponse
from .models import ChatUser
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def all_users(request):
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


@require_http_methods(["GET"])
def get_user(request, user_id):#12
    user = ChatUser.objects.filter(id=user_id).values()
    if len(user) == 0:
        return JsonResponse({'user':'does not exist'}, status=404)
    return JsonResponse({'user':list(user)})
# Create your views here.

