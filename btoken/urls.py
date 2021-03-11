from django.urls import path

from btoken import views as btoken_views
from . import views
urlpatterns=[
    #user/sms
    # http://192.168.0.105:8000/users/
    path('', btoken_views.TokensView.as_view()),
    # # user/get
    # # http://192.168.0.105:8000/users/145
    # path('<str:username>', views.UsersView.as_view()),
    # #user/post
    # #http://192.168.0.105:8000/users/
    # path('', views.UsersView.as_view()),
]
