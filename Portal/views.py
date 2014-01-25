from twisted.names.dns import NULL
from django.contrib.auth.management import get_default_username
from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from Portal.models import users , course , studentList

def index(request):
    return render(request,"home.html", {})
def profList(request):
    mylist=users.objects.get(accessLevel=2)
    return render(request,'user_List.html', {'userList': mylist})

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

def courseList(request):
    list = course.objects.all()
    return render(request,"courseList.html",{'list' : list})


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

def studentCourseList(request,studentId):
    stu = users.objects.get(Id= studentId)
    cs = studentList.objects.filter(student = stu)
    return render(request,"studentCourseList.html",{'list' : cs})

def addPoint(request,ListId,point):
    itm = studentList.objects.get(Id = ListId)
    itm.point = point
    itm.save()
    return classList(request,itm.course.teacherID.username)
def classList(request,usernameF):
    usr = users.objects.get(username = usernameF)
    prof = course.objects.filter(teacherID = usr)

    return  render(request,"profClassList.html",{'list' : prof })

def changePassword(request):
    return render(request,"changePassword.html",{})

def submitPassword(request,password):
    user = users.objects.get("")
    user.password = password
    user.save()

    return index(request)

'''

class StudentManager(ListView):
    model = users
    template_name = 'user_List.html'



class porfManager(ListView):
    model = users


class courseManager(ListView):
    model = course


'''


