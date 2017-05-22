# -*- coding: utf-8 -*-
# @Author: maomao
# @Date:   2016-12-02 14:41:12
# @Last Modified by:   maomao
# @Last Modified time: 2016-12-02 15:13:12
from django.conf.urls import url
import views


urlpatterns = [
	url(r'^$',views.captcha,name='manager_captcha'),
]	