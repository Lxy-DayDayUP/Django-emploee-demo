from django.shortcuts import render, redirect,HttpResponse
from app01 import models
from app01.utils.Forms import loginModelForm
from app01.utils.code import check_code
from io import BytesIO
def login(request):
    if request.method == 'GET':
        form = loginModelForm()
        return render(request,'login.html',{'form':form})
    elif request.method == 'POST':
        form = loginModelForm(data=request.POST)
        if form.is_valid():
            # 先检查验证码
            input_code = form.cleaned_data.pop('code') #用pop，取得code后，还能把code从cleaned_data中删除，因为后面filter要用
            real_code = request.session.get('code') #生成验证码时存储在session中
            if input_code != real_code:
                form.add_error('code', '验证码错误')
                return render(request, 'login.html', {'form': form})
            #检查用户是否存在
            exit = models.Admin.objects.filter(**form.cleaned_data).first()
            if exit:
                #保存session
                request.session['info']={'username':exit.username,'id':exit.id}
                request.session.set_expiry(60*60*24)#设置有效期一天
                return redirect('/admin/list')
            else:
                form.add_error('password','用户名密码错误')
                return render(request, 'login.html', {'form': form})
        else:
            return render(request,'login.html',{'form':form})

def img_code(request):      #check_code()使用前要在项目文件中导入字体文件
    img,code = check_code() #借助这个函数生成（验证码图片，验证码字符串）
    stream = BytesIO() #借助这个对象，将图片存储到内存中
    img.save(stream,'png')
    request.session['code']=code #存储验证码，方便之后查找到并检验输入的是否正确
    request.session.set_expiry(60)#验证码60秒有效
    return HttpResponse(stream.getvalue())#给前端返回验证码图片

def logout(request):
    request.session.clear()
    return redirect('/login/')

def regist(request):
    if request.method == 'GET':
        form = loginModelForm()
        return render(request,'regist.html',{'form':form})
    elif request.method == 'POST':
        form = loginModelForm(data=request.POST)
        if form.is_valid():
            # 先检查验证码
            input_code = form.cleaned_data.pop('code')  # 用pop，取得code后，还能把code从cleaned_data中删除，因为后面filter要用
            real_code = request.session.get('code')  # 生成验证码时存储在session中
            if input_code != real_code:
                form.add_error('code', '验证码错误')
                return render(request, 'login.html', {'form': form})
            #检查用户是否存在
            print(form.cleaned_data)
            exit = models.Admin.objects.filter(username=form.cleaned_data['username']).first()
            if exit:
                form.add_error('username','用户名已存在')
                return render(request, 'login.html', {'form': form})
            else:
                models.Admin.objects.create(**form.cleaned_data)
                return HttpResponse('注册成功')
