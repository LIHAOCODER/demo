# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponse
from pure_pagination import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.

from .models import Course,CourseResource
from operation.models import UserFavorite,CourseComments

class CourseListView(View):
    def get(self,request):
        all_course=Course.objects.all().order_by('-add_time')

        hot_courses = Course.objects.all().order_by('-click_nums')[:3]

        #排序
        sort = request.GET.get('sort', '')
        if sort:
            if sort == 'students':
                all_course = all_course.order_by('-students')
            elif sort == 'hot':
                all_course = all_course.order_by('-click_nums')

        try:
            page = request.GET.get('page',1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_course,3,request=request)
        courses = p.page(page)


        return render(request,'course-list.html',{
            'all_course': courses,
            'sort':sort,
            'hot_courses':hot_courses,
        })


class CourseDetailView(View):
    """
    课程详情
    """
    def get(self,request,course_id):
        course = Course.objects.get(id=int(course_id))
        #增加课程点击数
        course.click_nums += 1
        course.save()
        #是否收藏课程
        has_fav_course = False
        #是否收藏机构
        has_fav_org = False

        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user,fav_id=course_id,fav_type=1):
                has_fav_course =True
            if UserFavorite.objects.filter(user=request.user,fav_id=course.cource_org_id,fav_type=2):
                has_fav_org = True

        tag = course.tag
        if tag:
            relate_course = Course.objects.filter(tag=tag)[:1]
        else:
            relate_course = []
        return render(request, 'course-detail.html', {
            'course':course,
            'has_fav_course':has_fav_course,
            'has_fav_org':has_fav_org,
            'relate_course':relate_course,
        })

class CourseInfoView(View):
    """
    课程章节信息
    """
    def get(self,request,course_id):
        course = Course.objects.get(id=int(course_id))
        all_resources = CourseResource.objects.filter(course=course)
        return render(request, 'course-video.html', {
            'course':course,
            'all_resources':all_resources,
        })


class CourseCommentsView(View):
    """
    课程评论
    """
    def get(self,request,course_id):
        course = Course.objects.get(id=int(course_id))
        all_resources = CourseResource.objects.filter(course=course)
        all_comments = CourseComments.objects.all()
        return render(request, 'course-comment.html', {
            'course':course,
            'all_resources':all_resources,
            'all_comments':all_comments,
        })

class AddComentsView(View):
    """
    用户添加课程评论
    """
    def post(self,request):
        if not request.user.is_authenticated():
            #判断用户登录状态
            return HttpResponse('{"status":"fail","msg":u"用户未登录"}', content_type="application/json")
        course_id = request.POST.get("course_id",0)
        comments = request.POST.get("comments","")
        if course_id > 0 and comments:
            course_comments = CourseComments
            course = Course.objects.get(id=int(course_id))
            course_comments.course = course
            course_comments = comments
            course_comments.user = request.user
            course_comments.save()
            return HttpResponse('{"status":"success","msg":u"添加成功"}', content_type="application/json")
        else:
            return HttpResponse('{"status":"fail","msg":u"添加失败"}', content_type="application/json")

class VideoView(View):
    def post(self,request):
        """
        视频播放
        """
        if not request.user.is_authenticated():
            #判断用户登录状态
            return HttpResponse('{"status":"fail","msg":u"用户未登录"}', content_type="application/json")
        course_id = request.POST.get("course_id",0)
        comments = request.POST.get("comments","")
        if course_id > 0 and comments:
            course_comments = CourseComments
            course = Course.objects.get(id=int(course_id))
            course_comments.course = course
            course_comments = comments
            course_comments.user = request.user
            course_comments.save()
            return HttpResponse('{"status":"success","msg":u"添加成功"}', content_type="application/json")
        else:
            return HttpResponse('{"status":"fail","msg":u"添加失败"}', content_type="application/json")


