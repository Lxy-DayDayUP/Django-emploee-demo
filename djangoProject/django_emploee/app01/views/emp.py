from django.shortcuts import render, redirect
from app01 import models
from app01.utils.pagenation import Pagenation
from app01.utils.Forms import mymodel
def user_list(request):
    emp_list = models.emp.objects.all()
    obj = Pagenation(request,emp_list)
    return render(request, 'emp_list.html', {'emplist': obj.currentpage_data(),'page_str':obj.html()})

def user_add(request):
    if request.method == 'GET':
        contex = {
            'gdchoice': models.emp.gender_choice,
            'deplist': models.Department.objects.all()
        }
        return render(request, 'emp_add.html', contex)
    elif request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        pwd = request.POST.get('pwd')
        acount = request.POST.get('acount')
        hiretime = request.POST.get('hiretime')
        gender = request.POST.get('gender')
        dname = request.POST.get('dname')
        models.emp.objects.create(name=name, age=age, password=pwd, account=acount, hiretime=hiretime, gender=gender,
                                  deptno_id=dname)
        return redirect('/user/list/')

def user_modelform_add(request):
    if request.method == 'GET':
        form = mymodel()
        contex = {
            'title': '新建用户',
            'form': form
        }
        return render(request, 'change.html', contex)
    elif request.method == 'POST':
        form = mymodel(data=request.POST)
        contex = {
            'title': '新建用户',
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('/user/list')
        else:
            return render(request, 'change.html', contex)

def emp_edit(request, nid):
    ed_obj = models.emp.objects.filter(id=nid).first()
    form = mymodel(instance=ed_obj)
    emplist = models.emp.objects.all()
    if request.method == 'GET':
        return render(request, 'emp_edit.html', {'emplist': emplist, 'nid': nid, 'md': form})
    elif request.method == 'POST':
        form = mymodel(data=request.POST, instance=ed_obj)
        if form.is_valid():
            form.save()
            return redirect('/user/list')
        else:
            return render(request, 'emp_edit.html', {'emplist': emplist, 'nid': nid, 'md': form})