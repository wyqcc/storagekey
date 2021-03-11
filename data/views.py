from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from tools.logging_dec import logging_check
from data.models import Data
import json
from user.models import User
import time


@logging_check
def data(request):
    if request.method == 'GET':
        data_all = Data.objects.all()
        result = []
        for install in data_all:
            table = {'id': install.id, 'user_id': install.user_id.username, 'url_name': install.url_name,
                     'url': install.url,
                     'user_name': install.user_name, 'user_password': install.user_password, 'remarks': install.remarks,
                     'establish_time': install.establish_time}
            result.append(table)
        result = {'code': 200, 'result': result}
        return JsonResponse(result)

    elif request.method == 'POST':
        json_str = request.body
        json_obj = json.loads(json_str)
        url_name = json_obj['url_name']
        url = json_obj['url']
        user_name = json_obj['user_name']
        user_password = json_obj['user_password']
        remarks = json_obj['remarks']
        user = request.myuser
        dic = {'user_id': user, 'url_name': url_name,
               'url': url,
               'user_name': user_name, 'user_password': user_password, 'remarks': remarks}
        Data.objects.create(**dic)
        result = {'code': 200}
        return JsonResponse(result)

    elif request.method == 'DELETE':
        json_str = request.body
        json_obj = json.loads(json_str)
        data_id = json_obj['data_id']
        Data.objects.filter(id=data_id).delete()
        result = {'code': 200}
        return JsonResponse(result)

    elif request.method == 'PUT':
        json_str = request.body
        json_obj = json.loads(json_str)
        id = json_obj['data_id']
        url_name = json_obj['url_name']
        url = json_obj['url']
        user_name = json_obj['user_name']
        user_password = json_obj['user_password']
        remarks = json_obj['remarks']
        Data.objects.filter(id=id).update(url_name=url_name, url=url, user_name=user_name, user_password=user_password,
                                          remarks=remarks)
        result = {'code': 200}
        return JsonResponse(result)
