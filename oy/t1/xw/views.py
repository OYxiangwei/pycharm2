from django.shortcuts import render,render_to_response
from django.http import HttpResponse,Http404
from django.core.urlresolvers import reverse

# Create your views here.
def do_normalmap(request):
   return HttpResponse("this is nomalmap")

def withparam(request,year,month):
    return HttpResponse("today {0} ,{1}".format(year,month))

def do_app(r):
    return HttpResponse("子路由")
def showpg(r,pn):
    return HttpResponse("now is {}".format(pn))
def extremparam(request,name):
    return HttpResponse("名字：{}".format(name))
def revparse(request):
    return HttpResponse("you url {0}".format(reverse("askname")))
def exception(request):
    raise Http404

def v8(request):
    rst = ""
    for k,v in request.GET.items():
        rst += k+"..."+v

    return HttpResponse("结果{0}".format(rst))

def v9_get(request):
    return render_to_response("for_post.html")

def v9_post(request):
    rst= ""
    for k,v in request.POST.items():
        rst += k + "..." + v
    return HttpResponse("结果:{0}".format(rst))
def render1(request):
    c=dict()
    c['name']="hacker"
    rsp = render(request,"render1.html",context=c)
    return rsp

def render2(request):
    from django.template import loader
    t = loader.get_template("render1.html")
    print(type(t))
    r = t.render({"name":"欧阳"})
    print(type(r))
    return HttpResponse(r)
def render3(request):
    rsp = render_to_response("render1.html",context={"name":"欧阳锦煦"})
    return rsp
def get404(request):
    from django.views import defaults
    return defaults.page_not_found(request,Exception)


def e(r):
    pass