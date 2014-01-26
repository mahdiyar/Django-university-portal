from django.shortcuts import render
from  Portal.forms import LoginForm, addCourse,addPoint,userInfo,point,courses
from django.contrib.auth import  authenticate, login , logout
# Create your views here.
from django.views.generic.list import ListView
from Portal.models import  course , studentList
from django.http import  HttpResponseRedirect , request
from django.contrib.auth.decorators import  login_required

@login_required
def index(request):
    return render(request,"home.html", {})

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username,password = password)
        if user is not  None:
            login(request,user)
            return HttpResponseRedirect("/Home/")
        else:
            return  render(request,"login.html")

    else:
        return render(request,"Login.html")


def courseList(request):
    list = course.objects.all()
    return render(request,"courseList.html",{'list' : list})


def classList(request,courseId):
    list = studentList.objects.filter(id = courseId)
    courseObj = list.first().course.name
    return  render(request,"classList.html",{'list' : list,'course' : courseObj})

def studentCourseList(request):
    cs = studentList.objects.filter(student = request.user)
    return render(request,"studentCourseList.html",{'list' : cs})

@login_required
def points(request):
    return  render(request,"points.html",{'form' : point()})

def addPoint(request,ListId,point):
    itm = studentList.objects.get(Id = ListId)
    itm.point = point
    itm.save()
    return classList(request,itm.course.teacherID.username)
"""
def classList(request,usernameF):
    usr = users.objects.get(username = usernameF)
    prof = course.objects.filter(teacherID = usr)

    return  render(request,"profClassList.html",{'list' : prof })
"""

@login_required
def userSetting(request):
    tmp = userInfo({'model' :request.user})
    return render(request,"setting.html",{'form' : userInfo(instance=request.user)})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect("/Login/")


"""
def addProf(request):
    return  render(request,"add_prof.html",{})
def submitProf(request):
    usernameF = request.POST['']
    passwordF = request.POST['']
    emailF = request.POST['']
    nameF = request.POST['']
    prof= users(username= usernameF,password=passwordF,email=emailF,name=nameF)
    prof.save()
    return  profList(request)

def removeProf(request,userId):
    prof = users.objects.get(Id = userId)
    prof.delete()
    return profList(request)


def addCourse(request):
    return render(request,"addCourse.html",{})

def submitCourse(request):
    nameF = request.POST['']
    descriptionF = request.POST['']
    teacherNameF = request.POST['']
    t= users.objects.get(username = teacherNameF)
    c = course(description = descriptionF, name = nameF,status= True,teacherID = t)
    c.save()
    return courseList(request)

def removeCourse(request,courseId):
    c = course.objects.get(Id = courseId)
    c.status = False
    c.save()
    return  courseList(request)

"""

