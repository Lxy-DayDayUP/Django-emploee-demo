from django.shortcuts import render, redirect
from app01 import models
from app01.utils.Forms import AdminModelForm

def admin_list(request):
    obj = models.Admin.objects.all()
    form = AdminModelForm()
    contex = {
        'obj':obj,
        'form':form
    }
    return render(request,'admin_list.html',contex)

def admin_add(request):
    if request.method == 'GET':
        form = AdminModelForm()
        contex = {
            'title': '新建管理员',
            'form': form
        }
        return render(request, 'change.html', contex)
    elif request.method == 'POST':
        form = AdminModelForm(data=request.POST)
        contex = {
            'title': '新建管理员',
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('/admin/list')
        return  render(request, 'change.html', contex)

def admin_reset(request,nid):
    obj = models.Admin.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = AdminModelForm(instance=obj)
        contex = {
            'title':'重置密码--{}'.format(obj.username),
            'form':form
        }
        return render(request,'change.html',contex)
    elif request.method == 'POST':
        form = AdminModelForm(data=request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/admin/list')
        contex = {
            'title':'重置密码--{}'.format(obj.username),
            'form':form
        }
        return render(request,'change.html',contex)
