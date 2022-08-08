from django.shortcuts import render,HttpResponse,redirect
import requests
from app01.models import user_info
# Create your views here.
def index(request):
    return HttpResponse("Hello")

def news(req):
    return render(req, "news.html")

def login(request):
    if request.method == "GET": # 如果用户发来的请求方式是GET，就进如登录页面
        return render(request,'login.html')
    if request.method == "POST":#如果用户发来的请求方式是POST，就验证用户名密码，正确就返回登录成功页面
       if request.POST.get('user') == 'lxy' and request.POST.get('pwd') == '123':
            return HttpResponse("登陆成功")
       else:
           loginfail = '用户名密码错误'#用户名密码错误，返回登录页面，并给html文件传入参数n1，页面会显示n1的值
           return render(request,'login.html',{'n1':loginfail})

def userlist(request):
    userlist = user_info.objects.all()
    return render(request,'userlist.html',{'userlista':userlist})

def useradd(request):
    if request.method == "GET":
        return render(request, 'useradd.html')
    if request.method == 'POST':
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        age = request.POST.get('age')
        user_info.objects.create(name=user, password=pwd, age=age)
        return redirect('/userlist/')

def userdelete(request):
    nid = request.GET.get('nid')
    user_info.objects.filter(id = nid).delete()
    return redirect('/userlist/')
