from django.urls import path
from . import views
urlpatterns=[
    #user/sms
    # http://127.0.0.1:8000/users/sms
    path('sms', views.sms_view),
    # user/get
    # http://192.168.0.105:8000/users/145
    path('<str:username>', views.UsersView.as_view()),
    # user/post
    # http://192.168.0.105:8000/users/
    path('', views.UsersView.as_view()),
]