from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, Http404


# Create your views here.
def do_normalmap(request):
    return HttpResponse('this is normalmap')
def withparam(request,year,month):
    return HttpResponse("this is with param year{0}、month{1}".format(year,month))
def do_app(request):
    return HttpResponse("走子路由")
def pg(request,pn):
    return HttpResponse("the page number is :{}".format(pn))
def myname(request,name):
    return HttpResponse("myname is :{}".format(name))

def revparse(request):
    return HttpResponse("you request url is {}".format(reverse("askname")))
def v10_1(request):
    return HttpResponseRedirect("/v11")
def v10_2(request):
    return HttpResponseRedirect(reverse("v11"))
def v11(request):
    return HttpResponse("哈哈，这是v11的访问返回")
def v2_exception(request):
    #raise Http404
    return HttpResponse("ok")
def v8_get(request):
    rst = ""
    for k,v in request.GET.items():
        rst += k + "--->" + v
        rst += ","
    return HttpResponse("get value of request is :{0}".format(rst))
def v9_get(request):
    return render_to_response("for_post.html")

def v9_post(request):
    rst = ""
    for k,v in request.POST.items():
        rst += k + "--->" + v
        rst += ","
    return HttpResponse("get value of POST is :{0}".format(rst))
def render_test(request):
    rsp = render(request,"render.html")
    #rsp = HttpResponse(request,"render.html")
    return rsp
def render_test2(request):
    c = dict()
    c["name"]= "欧阳文宸"
    rsp = render(request,"render.html",context=c)
    return rsp
def render_test3(request):
    from django.template import loader
    t =loader.get_template("render.html")
    print(type(t))
    r = t.render({'name':"Anonymous"})
    print(type(r))
    return HttpResponse(r)
def render_test4(request):
    rsp = render_to_response("render.html",context={"name":"超人"})
    return rsp
def get404(request):
    from django.views import defaults
    return defaults.page_not_found(request,Exception)
def two(request):
    c = dict()
    c["name"] = "欧阳文宸"
    c["2name"] = "oy"
    return render(request,'render.html',context=c)
def three(request):
    ct = dict()
    ct['score']=[11,22,33,44]
    return render(request,'render.html',context=ct)
def four(request):
    ct = dict()
    ct['i'] = 1
    return render(request,'render.html',context=ct)
def five_post(request):
    print(request.POST)
    return render(request,'d.html')
def mysess(request):
    print(type(request.session))
    print(request.session)
    print(request.session.get('teacher_name','NoName'))
    request.session.clear()
    print("in mysess")
    return None
def student(request):
    stus = student.objects.all()
    p = Paginator(stus,40)
    print(p.count)
    print(p.page_range)
    print(p.num_pages)
    print(p.page_range)
    p.page(3)
    return stus
