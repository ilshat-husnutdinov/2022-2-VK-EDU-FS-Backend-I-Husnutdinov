from django.http import JsonResponse, HttpResponse
from .models import AppUser
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from users.serializers import AppUserSerializer


class AllUsersList(ListCreateAPIView):
    serializer_class = AppUserSerializer
    queryset = AppUser.objects.all()


class UserInfo(RetrieveUpdateDestroyAPIView): # 12 (получить информацию о пользователе)
    serializer_class = AppUserSerializer

    def get_queryset(self):
        chat_user_id = self.kwargs['pk']
        return AppUser.objects.filter(id=chat_user_id)


# ФУНКЦИОНАЛЬНЫЕ ВЬЮХИ ИЗ ДЗ6
# @require_http_methods(["GET"])
# def all_users(request):
#     users = AppUser.objects.select_related()
#     users_info = [
#         {
#             'id':user.id,
#             'username':user.username,
#             'first-name':user.first_name,
#             'gender':user.gender,
#         }
#         for user in users
#     ]
#     return JsonResponse({'users':users_info})


# @require_http_methods(["GET"])
# def get_user(request, user_id):#12
#     user = AppUser.objects.filter(id=user_id).values()
#     if len(user) == 0:
#         return JsonResponse({'user':'does not exist'}, status=404)
#     return JsonResponse({'user':list(user)})
# # Create your views here.
