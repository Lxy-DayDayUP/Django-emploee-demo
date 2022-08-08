from django.shortcuts import render, redirect,HttpResponse
from app01.utils.Forms import TaskModelForm
from django.views.decorators.csrf import csrf_exempt
import json
def task_list(request):
    form = TaskModelForm()
    return render(request,'task_list.html',{'form':form})

@csrf_exempt
def task_add(request):
    form = TaskModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        data_dict = {'status':True}
        return HttpResponse(json.dumps(data_dict))
    else:
        data_dict = {'status':False,'errors':form.errors}
        return HttpResponse(json.dumps(data_dict))
