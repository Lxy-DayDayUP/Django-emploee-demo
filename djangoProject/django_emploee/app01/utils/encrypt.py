import  hashlib
from django.conf import settings
def md5(string):
    '''传入一个字符串，返回字符串的md5值'''
    obj = hashlib.md5(settings.SECRET_KEY.encode('utf-8'))
    obj.update(string.encode('utf-8'))
    return obj.hexdigest()