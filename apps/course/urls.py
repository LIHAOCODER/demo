# _*_ coding: utf-8 _*_
__author__ = 'lihao'
__date__ = '2017/12/1 8:43'


from django.conf.urls import url,include
from .views import CourseListView,CourseDetailView,CourseInfoView,CourseCommentsView,AddComentsView

urlpatterns = [
    #课程列表
    url(r'^list/$',CourseListView.as_view(),name='course_list'),
    #课程详情
    url(r'^detail/(?P<course_id>.*)/$',CourseDetailView.as_view(),name='course_detail'),

    url(r'^info/(?P<course_id>.*)/$',CourseInfoView.as_view(),name='course_info'),
    #课程评论
    url(r'^comment/(?P<course_id>.*)/$',CourseCommentsView.as_view(),name='course_comment'),
    #添加课程评论
    url(r'^comment/$',AddComentsView.as_view(),name='add_comment'),

    url(r'^video/(?P<video_id>.*)/$',CourseCommentsView.as_view(),name='course_video'),

]