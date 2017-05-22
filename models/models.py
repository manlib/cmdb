# _*_ coding:utf-8 _*_
from django.db import models

class Department(models.Model):
    sn = models.CharField(u'部门编号',max_length=32)
    name = models.CharField(u'部门名称',max_length=32)
    leader = models.ForeignKey('Employee',verbose_name=u'部门领导',blank=True,null=True)
    memo = models.TextField(u'备注',blank=True,null=True)
    superior = models.ForeignKey('Department',verbose_name=u'上级部门',blank=True,null=True)

    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = u'部门信息表'
        verbose_name_plural = u'部门信息表'



class Employee(models.Model):
    name = models.CharField(u"员工姓名",max_length=32)
    asset = models.OneToOneField('OfficeAsset',verbose_name=u'资产',blank=True,null=True)
    position = models.CharField(u'职位',max_length=32,blank=True,null=True)
    depart = models.ForeignKey('Department',verbose_name=u'部门')
    emp_sn = models.IntegerField(u'员工编号',unique=True)

    Sex = (
        (0, u'男'),
        (1, u'女')
    )
    sex = models.IntegerField(u'性别',choices=Sex,default=0)
    birth = models.DateField(u'员工出生日期',blank=True,null=True)
    hometown = models.TextField(u'祖籍',blank=True,null=True)
    address = models.TextField(u'现住地址',blank=True,null=True)
    phone = models.BigIntegerField(u'手机号码',blank=True,null=True)
    contacts = models.CharField(u'紧急联系人',max_length=32,blank=True,null=True)
    con_phone = models.BigIntegerField(u'联系人号码',blank=True,null=True)
    joined_date = models.DateField(u'入职时间',blank=True,null=True)
    leave_date = models.DateField(u'离职时间',blank=True,null=True)
    Status = (
        ('on', u'在职'),
        ('dimission', u'离职'),
        ('vacation', u'休假')
    )
    status = models.CharField(u'在职状态',choices=Status,max_length=64,default='on')
    memo = models.TextField(u'备注',blank=True,null=True)

    def __unicode__(self):
        return '%s-%s'%(self.emp_sn,self.name)
    class Meta:
        verbose_name = u'员工信息表'
        verbose_name_plural = u'员工信息表'


class OfficeAsset(models.Model):
    asset_type_choices = (
        ('pc',u'台式电脑'),
        ('note_pc',u'笔记本电脑'),
        ('printer',u'打印机'),
        ('other',u'其他')
    )
    status_choices = (
        (0,u'使用中'),
        (1,u'未使用'),
        (2,u'故障中'),
        (3,u'报修中'),
        (4,u'报废'),
        (5,u'未知')
    )
    sn = models.CharField(u'资产编号',max_length=128,unique=True)
    asset_type = models.CharField(u'资产类型',choices=asset_type_choices,max_length=64)
    asset_stauts = models.IntegerField(u'资产状态',choices=status_choices,default=0)
    asset_depart = models.ForeignKey('Department',verbose_name=u'资产所属部门',blank=True,null=True)
    manufactory = models.ForeignKey('ManuFactory',verbose_name=u'品牌',blank=True,null=True)
    product_no = models.CharField(u'型号',blank=True,null=True,max_length=32)
    agents = models.ForeignKey('Agents',verbose_name=u'代理商',blank=True,null=True)
    trade_date = models.DateField(u'购买时间', null=True, blank=True)
    expire_date = models.DateField(u'过保修期', null=True, blank=True)
    price = models.FloatField(u'价格', null=True, blank=True)
    create_date = models.DateTimeField(blank=True, auto_now_add=True)
    update_date = models.DateTimeField(blank=True, auto_now=True)
    memo = models.TextField(u'备注',blank=True,null=True)

    class Meta:
            verbose_name_plural = u'办公资产表'
            verbose_name = u'办公资产表'

class ManuFactory(models.Model):
    name = models.CharField(u'品牌',max_length=32,blank=True,null=True,unique=True)
    support_num = models.CharField(u'支持电话',max_length=30,blank=True,null=True)
    memo = models.CharField(u'备注', max_length=128, blank=True,null=True)

    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = u'厂商'
        verbose_name_plural = u"厂商"

class Agents(models.Model):
    name = models.CharField(u'代理商名称',max_length=64,unique=True)
    contacts = models.CharField(u'联系人',max_length=32,null=True,blank=True)
    support_num = models.CharField(u'支持电话', max_length=30, blank=True,null=True)
    memo = models.CharField(u'备注', max_length=128, blank=True,null=True)

    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = u'代理商'
        verbose_name_plural = u"代理商"

class AssetUseinfo(models.Model):
    asset = models.ForeignKey('OfficeAsset',verbose_name=u'资产')
    info_choices = (
        (0,u'采购'),
        (1,u'领用'),
        (2,u'送修'),
        (3,u'报废'),
        (4,u'故障')
    )
    status = models.IntegerField(choices=info_choices,verbose_name=u'资产动态')
    creat_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        if self.status == 1:
            return u"%s: %s领用%s %s一台， SN号为%s。"%(self.creat_date,self.asset.employee.name,self.asset.manufactory.name,self.asset.product_no,self.asset.sn)
        else:
            return u"%s: %s%s %s 一台， SN号为%s。"%(self.creat_date,self.get_status_display(),self.asset.manufactory.name,self.asset.product_no,self.asset.sn)

    class Meta:
        verbose_name = u'资产动态表'
        verbose_name_plural = u'资产动态表'


class Ram(models.Model):
    asset = models.ForeignKey('OfficeAsset')
    sn = models.CharField(u'SN号', max_length=128, blank=True, null=True)
    model = models.CharField(u'内存型号', max_length=128)
    slot = models.CharField(u'插槽', max_length=64)
    capacity = models.IntegerField(u'内存大小(MB)')
    memo = models.CharField(u'备注', max_length=128, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, auto_now_add=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = u'内存'
        verbose_name_plural = u"内存"


class CPU(models.Model):
    asset = models.OneToOneField('OfficeAsset')
    cpu_model = models.CharField(u'CPU型号', max_length=128,blank=True)
    cpu_count = models.SmallIntegerField(u'物理cpu个数')
    cpu_core_count = models.SmallIntegerField(u'cpu核数')
    memo = models.TextField(u'备注', null=True,blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(blank=True,null=True)
    class Meta:
        verbose_name = u'CPU部件'
        verbose_name_plural = u"CPU部件"

class Disk(models.Model):
    asset = models.ForeignKey('OfficeAsset')
    sn = models.CharField(u'SN号', max_length=128, blank=True,null=True)
    slot = models.CharField(u'插槽位',max_length=64)
    manufactory = models.CharField(u'制造商', max_length=64, blank=True, null=True)
    model = models.CharField(u'磁盘型号', max_length=128,blank=True,null=True)
    capacity = models.FloatField(u'磁盘容量GB')
    disk_iface_choice = (
        ('SATA', 'SATA'),
        ('SAS', 'SAS'),
        ('SCSI', 'SCSI'),
        ('SSD', 'SSD'),
    )

    iface_type = models.CharField(u'接口类型', max_length=64,choices=disk_iface_choice,default='SAS')
    memo = models.TextField(u'备注', blank=True,null=True)
    create_date = models.DateTimeField(blank=True, auto_now_add=True)
    update_date = models.DateTimeField(blank=True,null=True)

    class Meta:
        verbose_name = u'硬盘'
        verbose_name_plural = u"硬盘"