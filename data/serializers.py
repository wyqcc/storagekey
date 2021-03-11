from rest_framework import serializers
from rest_framework.pagination import LimitOffsetPagination

from data.models import Data


class DataSerializer(serializers.ModelSerializer):
    # ModelSerializer和Django中ModelForm功能相似
    # Serializer和Django中Form功能相似
    class Meta:
        model = Data
        # 和"__all__"等价
        # fields = ('id', 'user_id', 'url_name', 'url', 'user_name', 'user_password', 'remarks', 'establish_time')
        fields = "__all__"
class StandardResultSetPagination(LimitOffsetPagination):
    # 默认每页显示的条数
    default_limit = 20
    # url 中传入的显示数据条数的参数
    limit_query_param = 'limit'
    # url中传入的数据位置的参数
    offset_query_param = 'offset'
    # 最大每页显示条数
    max_limit = None