from django.http import JsonResponse
from django.conf import settings
import jwt
from user.models import User


def logging_check(func):
    def wrap(request, *args, **kwargs):
        # 从请求头中获取token

        token = request.META['HTTP_TOKEN']
        if not token:
            result = {'code': 10403, 'error': 'please login'}
            return JsonResponse(result)
        # 校验token
        try:
            res = jwt.decode(token, settings.JWT_TOKEN_KEY,algorithms=['HS256'])
            # print(res)
        except Exception as e:
            print('-check login error %s-' % e)
            result = {'code': 10404, 'error': 'please login'}
            return JsonResponse(result)
        username = res['username']
        user = User.objects.get(username=username)
        request.myuser = user
        return func(request, *args, **kwargs)
    return wrap

# # 验证token
# def get_user_by_request(request):
#     token = request.META.get('token')
#     if not token:
#         return None
#     try:
#         res = jwt.decode(token, settings.JWT_TOKEN_KEY)
#     except Exception as e:
#         print('get user jwt error %s' % e)
#         return None
#     username = res['username']
#     return username
