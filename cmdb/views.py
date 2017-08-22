from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.


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

    # return HttpResponse("hello world!")
    return render(request,"index.html",)#第一个参数是固定的，第二个参数是我制定的文件