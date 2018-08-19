from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User


class RegisterUsernameView(APIView):
    """
    获取用户名个数:
    GET: /users/usernames/(?P<username>\w{5,20})/count/
    """

    def get(self, request, username):
        # 通过模型查询,获取用户名个数:
        count = User.objects.filter(username=username).count()
        context = {
            'count': count,
            'username': username
        }
        return Response(data=context)

