# _*_ coding:utf-8 _*_ 
_author_ = 'mlj'
_date_ = '2017/5/10 22:15'

import xadmin

from .models import EmailVerifyRecord,Banner

class EmailVerifyRecordAdmin(object):
    list_display=['code','email','send_type','send_time']
    search_fields=['code','email','send_type']
    list_filter=['code','email','send_type','send_time']

class BannerAdmin(object):
    list_display=['title','image','url','index']
    search_fields=['title','image','url','index']
    list_filter=['title','image','url','index']

xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)


