# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from models.models import Employee,Department,OfficeAsset,AssetUseinfo
import forms


def manager_login(request):
    if request.method == 'GET':
        return render(request,'manager_login.html')
    else:
        pass

##员工操作
def emp_list(request):
    if request.method == 'GET':
        empModel = Employee.objects.all()
        form = forms.AddempForm()
        return render(request,'emp/emp_list.html',{'emps':empModel,'form':form})

def emp_add(request):
    if request.method == 'GET':
        emp = forms.AddempForm()
        return render(request,'emp/emp_add.html',{'emp':emp})
    else:
        form = forms.AddempForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(u'成功')
        else:
            return JsonResponse(form.errors)

# 部门操作
def depart_list(request):
    if request.method == 'GET':
        departs = Department.objects.all()
        return render(request,'depart/depart_list.html',{'departs':departs})

def depart_add(request):
    if request.method == 'GET':
        dep = forms.AddpartForm()
        return render(request,'depart/add_depart.html',{'depart':dep})


#office资产操作
def asset_list(request):
    if request.method == 'GET':
        assets = OfficeAsset.objects.all()
        return render(request,'asset/asset_list.html',{'assets':assets})

def asset_add(request):
    pass


def asset_userinfo(request):
    infos  = AssetUseinfo.objects.all()
    return render(request,'asset/assetinfo.html',{'infos':infos})

