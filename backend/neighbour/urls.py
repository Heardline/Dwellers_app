from neighbour import views
from django.urls import path


urlpatterns = [
    path('',views.getRoutes),
    path('users/',views.getUsers),
    path('users/<str:pk>',views.getUser),
    path('users/create/',views.addUser)
]