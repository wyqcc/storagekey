from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
import json
from user.models import User
import hashlib
from user.views import make_token


# Create your views here.
class TokensView(View):
    def get(self, request):
        result = {'code': 404}
        print("-GET-")
        return JsonResponse(result)

    def post(self, request):
        json_str = request.body
        json_obj = json.loads(json_str)
        username = json_obj['username']
        password = json_obj['password']
        try:
            user = User.objects.get(username=username)
        except Exception as e:
            print('--log in error %s--' % e)
            result = {'code': 10200, 'error': '用户名或密码错误!'}
            return JsonResponse(result)

        md5 = hashlib.md5()
        md5.update(password.encode())
        if md5.hexdigest() != user.password:
            result = {'code': 10201, 'error': '用户名或密码错误!'}
            return JsonResponse(result)
        # 校验成功后,生成token
        token = make_token(username)

        result = {'code': 200, 'username': username,
                  'data': {'token': token}}
        print('csserv:',result)
        print("-NOT-GET-")
        return JsonResponse(result)
