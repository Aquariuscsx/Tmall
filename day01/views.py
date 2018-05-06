from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.views.decorators.http import require_GET, require_http_methods

"""
请求 HttpRequest
响应 HttpResponse
"""


# 主要 负责显示页面,如何去显示
@require_GET  # 限制请求方式
@require_http_methods(['GET', 'POST'])  # 一次多种请求方式
def home(request):
    # request.POST
    # request.GET
    # 获取请求方式
    # request.method
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    elif request.method == 'PUT':
        pass

    # request.POST.get('page', 1) 后面是默认值
    request.GET.getlist('love')

    # 获取请求的路径 不包跨域名
    # request.path
    # request.FILES.get() UPloadFiles 的文件 --重点---
    # 字典 = request.FILES.get('file')
    # filename
    # content_type
    # content 文件内容
    # http

    request.META
    # content_length 得到上传文件的大小
    # content_type

    # request.COOKI
    # ES

    return render(request, 'home.html')


# 重定向 妆发
def home1(request):
    # HttpResponse

    # HttpResponseRedirect
    # HttpResponseBadRequest  400错误
    # HttpResponseServerError 服务器错误 500
    # HttpResponseNotFound  404错误

    # render == HttpResponse  简写 转化
    # redirect  重定向
    return HttpResponse('hello')


def redirect_method(request):
    """
    重定向
    :param request:
    :return:
    """

    return redirect('http://baidu.com')


def render_method(request):
    """
    转化
    :param request:
    :return:
    """
    return render(request, 'home.html')


#
# class Home(View):
#     def login(self, request, *arg, **kwargs):
#         return render(request, '')

def login(request):
    return render(request, 'home.html')
