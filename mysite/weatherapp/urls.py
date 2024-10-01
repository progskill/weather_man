from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('add-member/', views.add_member),
    path('membersList/', views.members_list),
]