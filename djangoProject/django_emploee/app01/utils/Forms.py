from app01 import models
from django import forms
from app01.utils.encrypt import md5
from app01.utils.pagenation import Pagenation
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
class BootstrapModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", 'placeholder': field.label}
class mymodel(forms.ModelForm):
    name = forms.CharField(min_length=3, label='用户名')

    class Meta:
        model = models.emp
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", 'placeholder': field.label}
class nicenummodel(forms.ModelForm):
    num = forms.CharField(label='靓号', max_length=11, validators=[RegexValidator('^1\d{10}$', '手机号格式不正确')])

    def clean_num(self):
        '''检查输入的手机号是否已存在'''
        txt_num = self.cleaned_data['num']
        num_exist = models.niceNum.objects.filter(num=txt_num).exists()
        if num_exist:
            raise ValidationError('手机号已存在')
        return txt_num

    class Meta:
        model = models.niceNum
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, item in self.fields.items():
            item.widget.attrs = {'placeholder': item.label}
class nicenumEditmodel(nicenummodel):
    def clean_num(self):
        txt_num = self.cleaned_data['num']
        num_exit = models.niceNum.objects.exclude(id=self.instance.pk).filter(num=txt_num).exists()
        if num_exit:
            raise ValidationError('靓号已存在')
        return txt_num

class AdminModelForm(BootstrapModelForm):
    confirm_pwd = forms.CharField(label='确认密码',max_length=32,widget=forms.PasswordInput)
    class Meta:
        model = models.Admin
        fields = '__all__'
        widgets={
            'password':forms.PasswordInput,#用于设置在浏览器页面上密码不明文显示
                 }
    def clean_password(self):
        '''对密码加密'''
        pwd = self.cleaned_data.get('password')
        md5pwd = md5(pwd)
        exist = models.Admin.objects.filter(id=self.instance.pk,password=md5pwd).exists()
        if exist:#对于重置密码时，检查是否与上次的密码相同
            raise ValidationError('密码不能与上次相同')
        return md5(pwd)
    def clean_confirm_pwd(self):
        '''检查两次密码是否一致，并返回密码的md5值用于存储至数据库'''
        pwd = self.cleaned_data.get('password')
        confirm_pwd = self.cleaned_data.get('confirm_pwd')
        confirm_pwd = md5(confirm_pwd)
        if pwd != confirm_pwd:
            raise ValidationError('密码不一致')
        return confirm_pwd

class loginModelForm(BootstrapModelForm):
    code = forms.CharField(label='验证码')
    class Meta:
        model = models.Admin
        fields = '__all__'
        widgets={
            'password':forms.PasswordInput
        }

    def clean_password(self):
        return md5(self.cleaned_data.get('password'))

class TaskModelForm(BootstrapModelForm):
    class Meta:
        model = models.Task
        fields = '__all__'
        widgets = {
            'detail':forms.TextInput
        }



