import xadmin

from user.models import User

class UserAdmin(object):

    list_display = ['user_id', 'username','password','name','phone','email','department','user_type','establish_time','old_time']
    fields = ('user_id', 'username','password','name','phone','email','department','user_type')



#
# class BaseSetting(object):
#     enable_themes = True
#     use_bootswatch = True  # 调出主题菜单



xadmin.site.register(User,UserAdmin)


