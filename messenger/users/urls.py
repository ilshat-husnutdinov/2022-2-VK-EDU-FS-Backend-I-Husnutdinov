from django.urls import path
from users import views


urlpatterns = [
    path("all-users", views.all_users),
    path("user/<int:user_id>", views.get_user),
]
