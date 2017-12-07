# _*_ coding: utf-8 _*_
__author__ = 'lihao'
__date__ = '2017/11/24 11:37'

import xadmin


from .models import UserAsk,CourseComments,UserFavorite,UserMessage,UserCourse


class UserAskAdmin(object):
    list_display = ['name','mobile','course_name','add_time']
    list_filter = ['name','mobile','course_name','add_time']
    search_fields = ['name','mobile','course_name']


xadmin.site.register(UserAsk,UserAskAdmin)


class CourseCommentsAdmin(object):
    list_display = ['user','course','comments','add_time']
    list_filter = ['user','course','comments','add_time']
    search_fields = ['user','course','comments']


xadmin.site.register(CourseComments,CourseCommentsAdmin)


class UserFavoriteAdmin(object):
    list_display = ['user','course','fav_id','fav_type','add_time']
    list_filter = ['user','course','fav_id','fav_type','add_time']
    search_fields = ['user','course','fav_id','fav_type']


xadmin.site.register(UserFavorite,UserFavoriteAdmin)


class UserMessageAdmin(object):
    list_display = ['user','message','has_read','add_time']
    list_filter = ['user','message','has_read','add_time']
    search_fields = ['user','message','has_read']


xadmin.site.register(UserMessage,UserMessageAdmin)


class UserCourseAdmin(object):
    list_display = ['user','course','add_time']
    list_filter = ['user','course','add_time']
    search_fields = ['user','course']


xadmin.site.register(UserCourse,UserCourseAdmin)