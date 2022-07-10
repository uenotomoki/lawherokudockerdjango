from django.views.generic import TemplateView
from django.shortcuts import render
from django.http.response import JsonResponse
from django.conf import settings
import json, base64


# from django.views.generic import TemplateView
# from django.shortcuts import render
# # from .forms import SendUrlForm
# # from .js_scraping_20211230 import d202112
# # from .austlian_page import d20220217
# from django.http import HttpResponse


#投稿内容一覧表示クラス
class TopView(TemplateView):
    def __init__(self):
        self.params = {
            'user':'',
            'data':'',
            'data_user':'',
            'data_comment_num':[],
        }

    #@login_required
    def get(self,request):
        print('get')
        print('get')
        print('get')
        print('get')
        print('get')
        return render(request,'myapp/home.html',self.params)

    def post(self,request):
        print('post')
        data = {"image": "data:image/png;base64,", "message": 'image_base64'}
        response = JsonResponse(data)
        response['Access-Control-Allow-Origin'] = '*'
        response['Access-Control-Allow-Credentials'] = 'true'
        response['Access-Control-Allow-Headers'] = "X-Requested-With, X-Prototype-Version, X-CSRF-Token"
        response['Access-Control-Allow-Methods'] = "POST, GET, OPTIONS"
        return response

def ajax_number(request):
    print('post')
    print('post')
    print('post')
    print('post')
    print('post')
    # number1 = int(request.POST.get('number1'))
    # number2 = int(request.POST.get('number2'))
    # plus = number1 + number2
    # minus = number1 - number2
    # d = {
    #     'plus': plus,
    #     'minus': minus,
    # }
    d = {
        'plus': 'plus',
        'minus': 'minus',
    }
    return JsonResponse(d)







# class TopView(TemplateView):
#     # def __init__(self):
#     #     self.params = {
#     #         'user':'',
#     #         'data':'',
#     #         'data_user':'',
#     #         'data_comment_num':[],
#     #         'form_send_url':SendUrlForm(),
#     #     }

#     def get(self,request):
#         return render(request,'myapp/home.html',self.params)

#     # def post(self,request):
#     #     self.params['url_contents'] = request.POST['url_contents']

#     #     #self.params['data'] = main()
#     #     #self.params['data'] = d202112()
#     #     #self.params['data'] = d20220217()
#     #     a = d20220217()
#     #     print(a)

#     #     return HttpResponse(a[0])
#     #     #return render(request,'myapp/home.html',self.params)