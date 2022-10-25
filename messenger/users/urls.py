from django.urls import path
from users import views


urlpatterns = [
    path("all-users", views.all_users),
]
