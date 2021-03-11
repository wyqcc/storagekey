from django.contrib import admin

# Register your models here.
from data.models import Data


@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_id','url_name', 'url', 'user_name',
                    'user_password', 'remarks', 'establish_time']
    fields = ('url_name', 'user_id','url', 'user_name',
              'user_password', 'remarks', 'establish_time',)
