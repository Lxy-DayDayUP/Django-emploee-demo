"""django_emploee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app01.views import depart,emp,nicenum,Admin,account,task

urlpatterns = [
   # path('admin/', admin.site.urls),
    #部门管理
    path('depart/list/', depart.depart_list),
    path('depart/add/', depart.depart_add),
    path('depart/delete/', depart.depart_delete),
    path('depart/<int:nid>/edit/', depart.depart_edit),
    #员工管理
    path('user/list/', emp.user_list),
    path('user/add/', emp.user_add),
    path('user/modelform/add/', emp.user_modelform_add),
    path('user/<int:nid>/edit/', emp.emp_edit),
    #靓号管理
    path('nicenum/list/', nicenum.nicenum_list),
    path('nicenum/add/', nicenum.nicenum_add),
    path('nicenum/modelform/add/', nicenum.nicenum_modelform_add),
    path('nicenum/<int:nid>/edit/', nicenum.nicenum_edit),
    path('nicenum/<int:nid>/delete/', nicenum.nicenum_delete),
    #管理员管理
    path('admin/list/', Admin.admin_list),
    path('admin/add/', Admin.admin_add),
    path('admin/<int:nid>/reset/', Admin.admin_reset),
    #登录
    path('login/', account.login),
    path('logout/', account.logout),
    path('image/code/', account.img_code),
    #任务管理
    path('task/list/', task.task_list),
    path('task/add/', task.task_add),


]
