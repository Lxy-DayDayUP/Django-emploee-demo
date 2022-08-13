from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
class authMidware(MiddlewareMixin):
    def process_request(self,request):
        if request.path_info in ['/login/','/image/code/','/regist/']:
            return
        info_dict = request.session.get('info')
        if not info_dict:
            return redirect('/login/')


