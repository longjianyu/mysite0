from sys import modules

from django.shortcuts import render
from django.shortcuts import HttpResponse
from cmdb import models

# Create your views here.

user_list = [
    {"user":"long","pwd":"abc"},
    {"user":"aaa","pwd":"aaa"},
]


def index(request):
    '''
    通过index指向了url里views里的index()函数
    #request.POST
    #request.GET
    #如果是html页面，还需要修改settings里的内容，为了让django知道页面位置
    :param request: 参数必须要有，名称类似self的默认规则，可以修改
    封装了用户请求的所有内容
    :return:不能直接返回字符串，必须由HttpResponse封装起来，这是django的规则
    如果要返回html页面，就要用render方法，这是django提供的方法
    '''
    if request.method =="POST":
        username = request.POST.get("username",None)
        password = request.POST.get("password",None)
        print(username,password)
        #添加数据到数据库,将从用户接受的数据保存到数据库
    #     modules.UserInfo.objects.create()
    # #从数据库读取所有数据,从数据库读取所有行
    # user_list = modules.UserInfo.objects.all()
    # return HttpResponse("hello world!")
    # 第一个参数是固定的，第二个参数是我指定的文件
    # 动态页面中，第三个参数是关键,render方法接收第三参数是后台返回给浏览器的数据，
    # 谈事一个字典，data是定义的指针名，回本对应的html引用
    return render(request,"index.html",{"data":user_list})