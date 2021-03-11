from django.http import JsonResponse
from requests import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from data.serializers import DataSerializer
from tools.logging_dec import logging_check
from data.models import Data
import json
from django.utils.decorators import method_decorator


class PoemThreeAPI(APIView):
    @method_decorator(logging_check)
    def get(self, request):

        data_all = Data.objects.all().filter(user_id=request.myuser)
        result = []
        for install in data_all:
            table = {'id': install.id, 'user_id': install.user_id.username, 'url_name': install.url_name,
                     'url': install.url,
                     'user_name': install.user_name, 'user_password': install.user_password, 'remarks': install.remarks,
                     'establish_time': install.establish_time}
            result.append(table)
        result = {'code': 200, 'result': result}
        return JsonResponse(result)

    @method_decorator(logging_check)
    def post(self, request):
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

    @method_decorator(logging_check)
    def delete(self, request):
        json_str = request.body
        json_obj = json.loads(json_str)
        data_id = json_obj['data_id']
        try:
            Data.objects.filter(id=data_id, user_id=request.myuser).delete()
            result = {'code': 200}
            return JsonResponse(result)
        except Exception as e:
            result = {'code': 404}
            return JsonResponse(result)

    @method_decorator(logging_check)
    def put(self, request):
        json_str = request.body
        json_obj = json.loads(json_str)
        id = json_obj['data_id']
        url_name = json_obj['url_name']
        url = json_obj['url']
        user_name = json_obj['user_name']
        user_password = json_obj['user_password']
        remarks = json_obj['remarks']
        try:
            Data.objects.filter(id=id, user_id=request.myuser).update(url_name=url_name, url=url, user_name=user_name,
                                                                      user_password=user_password,
                                                                      remarks=remarks)
            result = {'code': 200}
            return JsonResponse(result)
        except Exception as e:
            result = {'code': 404}
            return JsonResponse(result)
