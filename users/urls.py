from django.urls import path
from .views import GetUsersAPIView, AddUsersAPIView

urlpatterns = [
    path('getUsers', GetUsersAPIView.as_view(), name="get-users"),
    path('addUsers', AddUsersAPIView.as_view(), name="add-users"),
]
