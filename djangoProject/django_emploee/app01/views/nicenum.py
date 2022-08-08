from django.shortcuts import render, redirect
from app01 import models
from app01.utils.pagenation import Pagenation
from app01.utils.Forms import nicenummodel,nicenumEditmodel

def nicenum_edit(request, nid):
    obj = models.niceNum.objects.filter(id=nid).first()
    nlist = models.niceNum.objects.all()
    if request.method == 'GET':
        form = nicenummodel(instance=obj)
        return render(request, 'nicenum_edit.html', {'form': form, 'numlist': nlist, 'nid': nid})
    elif request.method == 'POST':
        form = nicenumEditmodel(data=request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/nicenum/list')
        else:
            return render(request, 'nicenum_edit.html', {'form': form, 'numlist': nlist, 'nid': nid})

def nicenum_delete(request, nid):
    models.niceNum.objects.filter(id=nid).first().delete()
    return redirect('/nicenum/list/')

def nicenum_add(request):
    nlist = models.niceNum.objects.all()
    page_obj = Pagenation(request,nlist)
    form = nicenummodel()
    newid = 'new'
    if request.method == 'GET':
        return render(request, 'nicenum_add.html', {'nlist': page_obj.currentpage_data(), 'form': form, 'newid': newid})
    elif request.method == 'POST':
        form = nicenummodel(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/nicenum/list')
        else:
            return render(request, 'nicenum_add.html', {'nlist': nlist, 'form': form, 'newid': newid})

def nicenum_list(request):
    v = request.GET.get('search', '')
    serch_obj = models.niceNum.objects.filter(num__contains=v)
    page_obj = Pagenation(request,serch_obj)
    obj = page_obj.currentpage_data()

    return render(request, 'nicenum_list.html', {'nlist': obj, 'v': v,'page_li_str':page_obj.html()})

def nicenum_modelform_add(request):
    form = nicenummodel()
    if request.method == 'GET':
        context={
            'title':'新增靓号',
            'form':form
        }
        return render(request, 'change.html', context)
    elif request.method == 'POST':
        form = nicenummodel(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/nicenum/list')
        else:
            context = {
                'title': '新增靓号',
                'form': form
            }
            return render(request, 'change.html', context)
