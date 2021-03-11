# -*- coding: utf-8 -*-
# @time     : 2020/12/25 11:15
# @Author   : 王永琪
# @Site     : 
# @File     : view.py
# @Software : PyCharm
from django.http import HttpResponse, JsonResponse

from django.utils.decorators import method_decorator
from django.views import View
import json
from .models import User
import hashlib
# 在使用setting.py时,导入Django的模块
from django.conf import settings

import jwt
import time
from tools.logging_dec import logging_check

import random

# 短信验证
from django.core.cache import cache
from tools.sms import WangYongQi
from .tasks import send_sms
# 日志模块
import logging

# 日志对象
logger = logging.getLogger(__name__)


class UsersView(View):

    @method_decorator(logging_check)
    def get(self, request, username=None):
        if username:
            # 返回指定用户的信息
            try:
                user = User.objects.get(username=username)
            except Exception as e:
                print('get user error %s' % e)
                result = {'code': 10104, 'error': '用户名错误'}
                logger.error(f'{username}登陆失败')
                return JsonResponse(result)

            if request.GET.keys():
                # key是否在属性中
                data = {}
                for k in request.GET.keys():
                    if k == 'password':
                        continue
                    if hasattr(user, k):
                        data[k] = getattr(user, k)
                result = {'code': 200, 'username': username, 'data': data}
                logger.info(f'{username}get:/user/:{result}')
                return JsonResponse(result)

            else:
                result = {'code': 200, 'username': username,
                          'data': {
                              'username': user.username,
                              'email': user.email,
                              'phone': user.phone,
                              'name': user.username,
                              'user_type': user.user_type,
                              'establish_time': user.establish_time,
                              'old_time': user.old_time,
                          }}
                logger.info(f'{username}get:/user/:{result}')
                return JsonResponse(result)

        else:
            # 返回所有用户信息
            return HttpResponse('-返回所有用户信息-')

    def post(self, request):
        # 1.获取ajax请求提交的数据
        json_str = request.body
        # 2.将json串反序列化为对象
        json_obj = json.loads(json_str)
        # 3. 获取数据
        username = json_obj['username']
        password_1 = json_obj['password1']
        password_2 = json_obj['password2']
        email = json_obj['email']
        phone = json_obj['phone']
        #  获取验证码 (查看前端页面中,有没有将验证码传递过来)
        sms_num = json_obj['sms_num']
        # 验证码检查
        # 1 从redis中获取并判断验验证码是否为空
        # 生成键
        cache_key = f'sms_{phone}'
        old_code = cache.get(cache_key)
        if not old_code:
            print(old_code)
            result = {'code': 10113, 'error': '验证码错误'}
            logger.error(f'{username}post:/user/:{result}')
            return JsonResponse(result)
        # 2 把接收的用户输入的验证码与redis中的验证比较
        # 两者不相等,直接返回
        if int(sms_num) != old_code:
            result = {'code': 10114, 'error': '验证码错误'}
            # logger.error(f'{username}post:/user/:{result}')
            return JsonResponse(result)

        # 4. 数据检查
        # 4.1 用户名是否可用
        old_user = User.objects.filter(username=username)
        if old_user:
            result = {'code': 10100, 'error': '用户名已被占用!'}
            logger.error(f'{username}post:/user/:{result}')
            return JsonResponse(result)
        # 4.2 两次密码是否一致
        if password_1 != password_2:
            result = {'code': 10101, 'error': '两次密码不一致!'}
            logger.error(f'{username}post:/user/:{result}')
            return JsonResponse(result)
        # 4.3 密码hash处理
        md5 = hashlib.md5()
        md5.update(password_1.encode())
        password_m = md5.hexdigest()

        # 5.添加用户信息到数据库(需要做异常处理)
        try:
            user = User.objects.create(username=username,
                                       password=password_m,
                                       email=email,
                                       phone=phone,
                                       )
        except Exception as e:
            print('create error is %s' % e)
            result = {'code': 10102, 'error': '用户名已被占用!'}
            logger.error(f'{username}post:/user/:{result}')
            return JsonResponse(result)

        # 生成token并返回
        token = make_token(username)
        print(token)
        return JsonResponse({'code': 200, 'username': username,
                             'data': {'token': token}})

    # @log.info
    @method_decorator(logging_check)
    def put(self, request, username):
        # 拿数据
        json_str = request.body
        json_obj = json.loads(json_str)
        # 修改对象
        request.myuser.username = json_obj['username']
        request.myuser.name = json_obj['name']
        request.myuser.phone = json_obj['phone']
        request.myuser.email = json_obj['email']
        request.myuser.department = json_obj['department']
        request.myuser.user_type = json_obj['user_type']
        # request.myuser.info = json_obj['phone']
        # 保存到数据库
        request.myuser.save()

        # 返回
        result = {'code': 200,
                  'username': request.myuser.username}
        # logger.error(f'{username}post:/user/:{result}')
        return JsonResponse(result)


# 颁发token
# @log.info
def make_token(username, expire=3600 * 24):
    key = settings.JWT_TOKEN_KEY
    headers = settings.HEADERS
    now = time.time()
    payload = {'username': username, 'exp': now + expire}
    jwts = jwt.encode(payload, key, algorithm="HS256", headers=headers)
    logger.info(f'{username}post:/user/:{payload}-->{jwts}')
    return jwts


# @log.info
@logging_check
def user_avatar(request, username):
    if request.method != 'POST':
        print(1)
        result = {'code': 10105, 'error': '请使用POST请求'}
        return JsonResponse(result)
    user = request.myuser
    user.avatar = request.FILES['avatar']
    print(user.save())
    # logger.info()
    result = {'code': 200, 'username': user.username}

    return JsonResponse(result)


def sms_view(request):
    # 1 获取手机号
    json_str = request.body
    json_obj = json.loads(json_str)
    phone = json_obj['phone']
    # 生成键
    cache_key = f'sms_{phone}'
    print('cache_key:', cache_key)
    # 获取已经生成的验证码,防止用户刷新浏览器多次发送短信验证码
    old_code = cache.get(cache_key)
    if old_code:
        result = {'code': 10112, 'error': '请稍后再发送!'}
        return JsonResponse(result)

    # 2 生成验证码
    code = random.randint(1000, 9999)
    # print('-----code is %s-----' % code)
    # 3 存储到redis中
    cache.set(cache_key, code, 65)
    # 同步发送
    # 4 将验证码发送到用户手机
    # 4.1 我们向容联云服务器发送了https的请求,并返回响应
    x = WangYongQi(settings.SMS_ACCOUNT_ID,
                   settings.SMS_ACCOUNT_TOKEN,
                   settings.SMS_APP_ID,
                   settings.SMS_TEMPLATE_ID)
    # 假设在这儿阻塞了3秒
    res = x.run(phone, code)
    print('-send sms result is %s-' % res)
    # 异步发送 (生产者,投递任务后,立即返回)
    send_sms.delay(phone, code)
    # logger.info()
    return JsonResponse({'code': 200})
