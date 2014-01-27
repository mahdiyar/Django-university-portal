from django.forms import ModelForm
from Portal.models import  course , studentList
from django import forms
from django.contrib.auth.models import User
class LoginForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','password')

class changePassword(ModelForm):
    class Meta:
        model = User
        field = ('password')

class addCourse(ModelForm):
    pass

class addPoint(ModelForm):
    pass

class userInfo(ModelForm):
 #   password = forms.CharField(widget=forms.PasswordInput)
 #   email = forms.EmailField()
 #   first_name = forms.CharField(max_length=100)
 #   last_name = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ('email','first_name','last_name')

class point(ModelForm):
    class Meta:
        model = studentList
        fields = ('point','student')

class courses(ModelForm):
    class Meta:
        model = course
        fields = ('name','description')

class ClassPoints(ModelForm):
    class Meta:
        model = course
        fields = ('name','description','teacher')

