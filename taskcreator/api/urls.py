from django.conf.urls import url
from django.contrib import admin

from .views import (
    TaskListAPIView,
    TaskListPrivateAPIView,
    TaskDetailAPIView,
    TaskCreateAPIView,
    TaskUpdateAPIView,
    TaskDeleteAPIView,
    UserCreateAPIView,
    UserLoginAPIView

    )

from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^tasks/public/$', TaskListAPIView.as_view(), name="task-list"),
    url(r'^tasks/(?P<uid>[\w-]+)/private/$', TaskListPrivateAPIView.as_view(), name="task-list"),
    url(r'^login/$', csrf_exempt(UserLoginAPIView.as_view()), name='login'),
    url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
    url(r'^tasks/create/$', TaskCreateAPIView.as_view(), name="task-create"),
    url(r'^(?P<pk>[\w-]+)/tasks/$', TaskListAPIView.as_view(), name="user-private-task-list"),
    
    url(r'^tasks/(?P<pk>[\w-]+)/delete/$', TaskDeleteAPIView.as_view(), name="task-delete"), # pk is id of task
    url(r'^tasks/(?P<pk>[\w-]+)/edit/$', TaskUpdateAPIView.as_view(), name="task-edit"), # pk is id of task
    url(r'^tasks/(?P<pk>[\w-]+)/detail/$', TaskDetailAPIView.as_view(), name="task-detail"), # pk is id of task


]
