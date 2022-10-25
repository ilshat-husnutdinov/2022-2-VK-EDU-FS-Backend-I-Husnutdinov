from django.http import JsonResponse, HttpResponse
from .models import ChatUser

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
# Create your views here.
