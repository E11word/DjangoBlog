#-*- coding:utf-8 -*-
import logging
from django.shortcuts import render
from django.http import HttpResponseRedirect,response
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.paginator  import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
from django.db.models import Count
from models import  *
from forms import CommentForm,UserForm,RegisterForm

logger = logging.getLogger('liublog.views')
# Create your views here.
def global_setting(request):
    if request.user.is_authenticated():
        login_name = '退出'
        log_flag= 0
    else:
        login_name = '登录'
        log_flag= 1
    SITE_NAME = settings.SITE_NAME
    SITE_DESC = settings.SITE_DESC
    WEIBO_CSDN = settings.WEIBO_CSDN
    WEIBO_TENCENT = settings.WEIBO_TENCENT
    PRO_RSS = settings.PRO_RSS
    PRO_EMAIL = settings.PRO_EMAIL
    #分类信息
    category_list = Category.objects.all()
    #文章归档数据
    archive_list = Article.objects.distinct_date()
    #广告数据
    ad_list = Ad.objects.all()
    ad = ad_list[1]
    #标签云
    tag_list = Tag.objects.all()
    #友情链接
    link_list = Links.objects.all()
    #文章排行
    article_order_list = Article.objects.order_by('-click_count')[:6]
    #评论排行
    comment_count_list = Comment.objects.values('article').annotate(comment_count=Count('article')).order_by('-comment_count')
    article_comment_list = [Article.objects.get(pk=comment['article']) for comment in comment_count_list ][:6]
    #最新文章
    article_new_list = Article.objects.order_by('-date_publish')[:6]
        #获取ip
    ip = get_client_ip(request)
    ip_list = Ip.objects.filter(ip = ip)
    if ip_list :
        ip_count =Ip.objects.count()
    else:
        ip_a = Ip(ip=ip)
        ip_a.save()
        ip_count = Ip.objects.count()
    return locals()

#分页代码
def getPage(request, article_list):
    paginator = Paginator(article_list,4)
    try:
        page = int(request.GET.get('page',1))
        article_list = paginator.page(page)
    except (EmptyPage,InvalidPage,PageNotAnInteger):
        article_list = paginator.page(1)
    return article_list

#用户ip
def get_client_ip(request):
    try:
          real_ip = request.META['HTTP_X_FORWARDED_FOR']
          regip = real_ip.split(",")[0]
    except:
        try:
            regip = request.META['REMOTE_ADDR']
        except:
            regip = ""
    return regip

#首页
def index(request):
    try:
        #最新文章数据
        article_list = Article.objects.all()
        article_list = getPage(request, article_list)
    except Exception as e:
        logger .error(e)
    return render(request, 'index.html', locals())

#文章归档
def archive(request):
    try:
        #最新文章数据
        year = request.GET.get('year',None)
        month = request.GET.get('month',None)
        article_list = Article.objects.filter(date_publish__icontains = year+ '-' + month)
        article_list = getPage(request, article_list)
    except Exception as e:
        logger .error(e)
    return render(request, 'archive.html', locals())

#文章显示
def articlepage(request):
    try:
        id=request.GET.get('id',None)
        article = Article.objects.get(pk=id)
        #点击量统计
        article.click_count = article.click_count + 1
        article.save()
        #评论显示
        comment_list = article.comment_set.all()
    except Exception as e:
        logger .error(e)
    return render(request, 'articlepage.html', locals())


#文章分类
def articlecategory(request):
    try:
        id=request.GET.get('id',None)
        category = Category.objects.get(pk=id)
        article_list = Article.objects.filter(category = category)
        article_list = getPage(request, article_list)
    except Exception as e:
        logger .error(e)
    return render(request, 'articlecategory.html', locals())

#标签云归类
def articletag(request):
    try:
        id=request.GET.get('id',None)
        tag = Tag.objects.get(pk=id)
        article_list = Article.objects.filter(tag=tag)
        article_list = getPage(request, article_list)
    except Exception as e:
        logger .error(e)
    return render(request, 'articletag.html', locals())

#用户登录
def loginin(request):
    if request.method == 'POST':
        user_name = UserForm(request.POST)
        if user_name.is_valid():
            #获取表单用户密码
            username = user_name.cleaned_data['username']
            password = user_name.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return  HttpResponseRedirect('/',locals())
    else:
        user_name = UserForm()
    return render(request ,'loginin.html',locals())


#评论页面
@login_required(redirect_field_name='' , login_url='loginin')
def articlecomment(request):
    id=request.GET.get('id',None)
    article = Article.objects.get(pk=id)
    comment_list = article.comment_set.all()
    #com_user = us.user
    if request.method == 'POST':
        coment_data  = CommentForm(request.POST)
        if coment_data .is_valid():
            uuser = coment_data.cleaned_data['username']
            upassword = coment_data.cleaned_data['password']
            conten = coment_data.cleaned_data['content']
            c_user  = authenticate(username = uuser,password = upassword)
            if c_user :
                com = Comment(content=conten,user = c_user,article = Article.objects.get(pk=id))
                com.save()
                return HttpResponseRedirect('/articlepage/?id=%s'%id,locals())
            else:
                return HttpResponseRedirect('/register/',locals())
    else:
        coment_data  = CommentForm()
    return render(request,'articlecomment.html', locals())

#用户注册页面
def register(request):
    id=request.GET.get('id',None)
    if request.method == 'POST':
       data  = RegisterForm(request.POST)
       if data.is_valid():
           name = data.cleaned_data['username']
           c_user  = User.objects.filter(username = name)
           if c_user :
              return HttpResponseRedirect('/register/')
           email = data.cleaned_data['email']
           password = data.cleaned_data['password']
           password2 = data.cleaned_data['password2']
           if password != password2 :
                return HttpResponseRedirect('/register/')
           if password :
               user = User(username=name,password = password, email = email)
               user.set_password(password)  #哈希保存
               user.save()
               return HttpResponseRedirect('/')
    else:
        data  = RegisterForm(request.POST)
    return render(request,'register.html',locals())

#留言
def message(request):
    article = Article.objects.get(pk='3')
    return render(request, 'message.html',locals() )

#用户登录
def loggout(request):
    logout(request)
    return HttpResponseRedirect('/')





