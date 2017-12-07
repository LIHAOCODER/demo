# _*_ coding: utf-8 _*_
__author__ = 'lihao'
__date__ = '2017/11/24 11:14'

import xadmin

from .models import  CityDict,CourseOrg,Teacher


class CityDictAdmin(object):
    list_filter = ['name','desc','add_time']
    list_display = ['name','desc','add_time']
    search_fields = ['name','desc']


xadmin.site.register(CityDict,CityDictAdmin)


class CourseOrgAdmin(object):
    list_filer = ['name','desc','click_nums','fav_nums','image','address','city','add_time']
    list_display = ['name','desc','click_nums','fav_nums','image','address','city','add_time']
    search_fields = ['name','desc','click_nums','fav_nums','image','address','city']


xadmin.site.register(CourseOrg,CourseOrgAdmin)


class TeacherAdmin(object):
    list_filer = ['org__name','name','work_years','work_company','work_position','points','add_time','fav_nums']
    list_display = ['org','name','work_years','work_company','work_position','points','add_time','fav_nums']
    search_fields =['org','name','work_years','work_company','work_position','points','fav_nums']


xadmin.site.register(Teacher,TeacherAdmin)