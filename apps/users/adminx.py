# _*_ coding: utf-8 _*_
__author__ = 'lihao'
__date__ = '2017/11/24 9:42'

import xadmin
from xadmin import views
from .models import EmailVerifyRecord
from .models import Banner


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


xadmin.site.register(views.BaseAdminView,BaseSetting)


class GlobalSettings(object):
    site_title = '同桌慕课'
    site_footer= '慕课在线学习'
    menu_style = 'accordion'


xadmin.site.register(views.CommAdminView,GlobalSettings)


class EmailVerifyRecordAdmin(object):
    list_display = ['code','email','send_type','send_time']
    search_fields = ['code','email','send_type']
    list_filter = ['code','email','send_type','send_time']


xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)


class BannerAdmin(object):
    list_display = ['title','image','url','index','add_time']
    list_filter = ['title','image','url','index']
    search_fields = ['title','image','url','index','add_time']


xadmin.site.register(Banner,BannerAdmin)
