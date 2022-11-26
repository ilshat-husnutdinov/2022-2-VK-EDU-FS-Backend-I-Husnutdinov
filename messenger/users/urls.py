from django.urls import path
from users import views


urlpatterns = [
    path("all-users", views.AllUsersList.as_view()),
    path("user/<int:pk>", views.UserInfo.as_view()),
]
