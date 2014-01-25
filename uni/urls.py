from django.conf.urls import patterns, include, url

from django.contrib import admin
from Portal import views
from Portal.views import StudentManager, profList, addProf, courseList

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'uni.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    (r'^admin/', include(admin.site.urls)),
    (r'^edu/students/' , StudentManager.as_view()),
    (r'^edu/prof/$',profList),
    (r'^edu/prof/add',addProf),
    (r'^student/courseList' , courseList),
    (r'^edu/courseList' , courseList),
#    (r'^portal/$',uni.Portal.views.index),
#    (r'^portal/login',uni.Protal.views.login),
#    (r'^portal/changePass',uni.Protal.views.changePass),
#    (r'^portal/setting',uni.Protal.views.setting),
#    (r'^portal/student/courseList',uni.Protal.views.stuCourseList),
#    (r'^portal/student/score',uni.Protal.views.stuScore),
#    (r'^portal/prof/courseList',uni.Protal.views.profCourseList),
#    (r'^portal/prof/class/?P<course_id>\d+',uni.Protal.views.Profclass),
#    (r'^portal/edu/studentManager', views.StudentManager.as_view()),
#    (r'^portal/profManagment',uni.Protal.views.profManagment),
#    (r'^portal/courseManagment',uni.Protal.views.courseManagment),


)
