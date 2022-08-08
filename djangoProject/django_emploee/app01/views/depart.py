from django.shortcuts import render, HttpResponse, redirect
from app01 import models
def depart_list(request):
    dep_list = models.Department.objects.all()
    return render(request, 'depart_list.html', {'deplist': dep_list})

def depart_add(request):
    if request.method == 'GET':
        return render(request, 'depart_add.html')
    elif request.method == 'POST':
        dpname = request.POST.get('dname')
        models.Department.objects.create(dname=dpname)
        return redirect('/depart/list/')

def depart_delete(request):
    nid = request.GET.get('nid')
    models.Department.objects.filter(id=nid).delete()
    return redirect('/depart/list/')

def depart_edit(request, nid):
    if request.method == 'GET':
        dep_list = models.Department.objects.all()
        ed_dep = models.Department.objects.filter(id=nid).first()
        return render(request, 'depart_edit.html', {'edit': ed_dep, 'deplist': dep_list})
    elif request.method == 'POST':
        newdname = request.POST.get('dname')
        models.Department.objects.filter(id=nid).update(dname=newdname)
    return redirect('/depart/list/')

