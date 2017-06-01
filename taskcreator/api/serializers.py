
import operator
from taskcreator.models import Task
from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

from django.contrib.contenttypes.models import ContentType




from rest_framework.serializers import (
    CharField,
    EmailField,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError
    )


User = get_user_model()


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
        ]




class UserCreateSerializer(ModelSerializer):
    email = EmailField(label='Email Address')
    email2 = EmailField(label='Confirm Email')
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'email2',
            'password',
            
        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                        }
    def validate(self, data):
        return data


    def validate_email(self, value):
        data = self.get_initial()
        email1 = data.get("email2")
        email2 = value
        if email1 != email2:
            raise ValidationError("Emails must match.")
        
        user_qs = User.objects.filter(email=email2)
        if user_qs.exists():
            raise ValidationError("This user has already registered.")

        return value

    def validate_email2(self, value):
        data = self.get_initial()
        email1 = data.get("email")
        email2 = value
        if email1 != email2:
            raise ValidationError("Emails must match.")
        return value



    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        user_obj = User(
                username = username,
                email = email,
                first_name = first_name,
                last_name = last_name

            )
        user_obj.set_password(password)
        user_obj.save()
        return validated_data



class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField(required=False, allow_blank=True)
    email = EmailField(required=False, allow_blank=True, label='Email Address')
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password',
            'token',
            
        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                            }
    def validate(self, data):
        user_obj = None
        email = data.get("email", None)
        username = data.get("username", None)
        password = data["password"]
        if not email and not username:
            raise ValidationError("A username or email is required")
        user = User.objects.filter(
                Q(email=email)|
                Q(username=username)
            ).distinct()
        user = user.exclude(email__isnull=True).exclude(email__iexact='')
        print user
        if user.exists() and user.count()==1:
            user_obj = user.first()
        else:
            raise ValidationError("Email/Username is not valid.")
        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect password. Please try again.")
            else:
                data["username"] = user_obj.username
                data["id"] = user_obj.id
                payload = jwt_payload_handler(user_obj)
                token = jwt_encode_handler(payload)
                data["token"] = token

        return data


        
class TaskSerializer(ModelSerializer):

    #user = UserDetailSerializer()
    class Meta:
        model = Task
        fields = [
            'id',
            'user',
            'title',
            'description',
            'deadline',
            'is_private',
            'created_at'

        ]
class TaskCreateSerializer(ModelSerializer):

    class Meta:
        model = Task
        fields = [
            'id',
            'user',
            'title',
            'description',
            'deadline',
            'is_private'

        ]
