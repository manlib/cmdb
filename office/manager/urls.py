# _*_ coding:utf-8 _*_

from django.conf.urls import url,include
import views
import test
from rest_framework import routers
from res_views import *

router = routers.DefaultRouter()
router.register(r'emp', EmpViewSet)

urlpatterns = [
    url(r'^login/$',views.manager_login,name='manager_login'),
    url(r'^emp_list/$',views.emp_list,name='emp_list'),
    url(r'^depart_list/$',views.depart_list,name='depart_list'),
    url(r'^emp_add/$',views.emp_add,name='emp_add'),
    url(r'^depart_add/$',views.depart_add,name='depart_add'),
    url(r'asset_list',views.asset_list,name='asset_list'),
    url(r'asset_add',views.asset_add,name='asset_add'),
    url(r'asset_userinfo',views.asset_userinfo,name='asset_userinfo'),
    url(r'^test/$',test.test),
    url(r'^api/',include(router.urls))
]