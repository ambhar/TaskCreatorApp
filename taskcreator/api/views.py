from rest_framework.generics import (
        CreateAPIView,
        DestroyAPIView,
        ListAPIView, 
        RetrieveAPIView,
        RetrieveUpdateAPIView,
        UpdateAPIView,
    )

from rest_framework.permissions import (
        AllowAny,
        IsAuthenticated,
        IsAdminUser,
        IsAuthenticatedOrReadOnly,
    )


from django.contrib.auth import get_user_model
User = get_user_model()

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from taskcreator.models import Task
from .serializers import TaskSerializer,TaskCreateSerializer, UserCreateSerializer, UserLoginSerializer
from django.utils.decorators import method_decorator

#USER REGISTER AND LOGIN VIEWS

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer
    
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

# List Down all Public Tasks
class TaskListAPIView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    def get_queryset(self):
        tasks = Task.objects.filter(is_private=False)
        return tasks

# List Down Private Tasks by a user using UserID
class TaskListPrivateAPIView(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_url_kwarg = "uid" # user ID
    def get_queryset(self):
        user_id = self.kwargs.get(self.lookup_url_kwarg)
        tasks = Task.objects.filter(user=user_id)
        return tasks

class TaskDetailAPIView(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = TaskSerializer
    lookup_url_kwarg = "pk" # program ID
    queryset = Task.objects.all()
    def get_queryset(self):
        task_id = self.kwargs.get(self.lookup_url_kwarg)
        tasks = Task.objects.filter(id=task_id)
        return tasks


class TaskCreateAPIView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer
    permission_classes = [AllowAny]
    

class TaskUpdateAPIView(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]

class TaskDeleteAPIView(DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [AllowAny]

