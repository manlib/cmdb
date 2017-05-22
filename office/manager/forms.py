# _*_ coding:utf-8 _*_

from django import forms
from django.forms import ModelForm
from models import models

class AddempForm(ModelForm):

    class Meta:
        model = models.Employee
        fields = ['name','position','emp_sn','sex','depart','phone','status','joined_date','memo']

class AddpartForm(ModelForm):

    class Meta:
        model = models.Department
        fields = ['name','sn','leader','superior','memo']

class AddassetForm(ModelForm):

    class Meta:
        model = models.OfficeAsset
        fields = ['sn','asset_type','asset_stauts','asset_depart','manufactory','product_no','memo']