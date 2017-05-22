# -*- coding: utf-8 -*-
# @Author: maomao
# @Date:   2016-12-02 14:42:58
# @Last Modified by:   maomao
# @Last Modified time: 2016-12-02 15:29:46
from django.http import HttpResponse
from captcha.xtcaptcha import Captcha
from PIL import Image
try:
	from cStringIO import StringIO
except ImportError:
	from io import BytesIO as StringIO

def captcha(request):
	text,img = Captcha.gene_code()
	out = StringIO()
	img.save(out,'png')
	out.seek(0)
	response = HttpResponse(content_type='image/png')
	response.write(out.read())
	return response