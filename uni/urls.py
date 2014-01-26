from django.conf.urls import patterns, include, url
from django.contrib import admin
from Portal.views import   courseList, index , Login, userSetting , points, user_logout , classList ,studentCourseList,profCourseList

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'uni.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

# !!!!       add (?i) after ^ in the patterns for support incase sensitive urls !!!!!!

    (r'^admin/', include(admin.site.urls)),
#    (r'^(?i)edu/prof/add',addProf),
     (r'^(?i)Setting',userSetting),
    (r'^(?i)student/courseList' , courseList),
    (r'^student/classList/(\d{1,2})/$',classList),
    (r'^student/myCourses/',studentCourseList),
    (r'^(?i)edu/courseList' , courseList),
    (r'^(?i)Home/',index),
    (r'^(?i)Login/$',Login),
    (r'^(?i)$',index),
    (r'^prof/points',points),
    (r'^prof/myclasses',profCourseList),
    (r'^(?i)Logout/$',user_logout),
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
