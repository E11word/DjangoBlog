# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import  AbstractUser

# Create your models here.
#用户模型
class User(AbstractUser):
    avatar = models.ImageField(upload_to = 'avatar/%Y/%m', default = 'avatar/default.png',max_length = 200,verbose_name='头像')
    qq = models.CharField(max_length = 20, blank = True, null = True, verbose_name = 'QQ号码')
    mobile = models.CharField(max_length = 11, blank = True, null = True, verbose_name = '手机号码')


    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __unicode__(self):
        return self.username

#标签
class Tag(models.Model):
    name = models.CharField(max_length= 30,verbose_name= '标签名称')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

#分类
class Category(models.Model):
    name = models.CharField(max_length= 30,verbose_name= '分类名称')
    index = models.IntegerField(default= 999,verbose_name= '分类的排序')

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __unicode__(self):
        return self.name

#广告
class Ad(models.Model):
    title = models.CharField(max_length= 50,verbose_name= '广告标题')
    description = models.CharField(max_length= 200,verbose_name= '广告描述')
    image_url = models.ImageField(upload_to = 'ad/%Y/%m',verbose_name= '图片路径')
    callback_url = models.URLField(null= True,blank= True,verbose_name= '回调url')
    date_public = models.DateTimeField(auto_now_add=True, verbose_name= '发布时间')
    index = models.IntegerField(default= 999,verbose_name= '排列顺序（从小到大）')

    class Meta:
        verbose_name = '广告'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __unicode__(self):
        return self.title

#自定义一个文章Model管理器
class ArticleManager(models.Manager):
    def distinct_date(self):
        distinct_date_list = []
        date_list = self.values('date_publish')
        for date in date_list:
            date = date['date_publish'].strftime('%Y年%m月文章')
            if date not in distinct_date_list:
                distinct_date_list.append(date)
        return distinct_date_list

#文章模型
class Article(models.Model):
    title = models.CharField(max_length= 50,verbose_name= '文章标题')
    description = models.CharField(max_length= 50,verbose_name= '文章描述')
    content = models.TextField(verbose_name= '文章内容')
    click_count = models.IntegerField(default= 0,verbose_name= '点击次数')
    is_recommend = models.BooleanField(default= False, verbose_name= '是否推荐')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name= '发布时间' )
    user = models.ForeignKey(User,verbose_name= '用户')
    category = models.ForeignKey(Category,blank= True,null= True, verbose_name= '分类')
    tag = models.ManyToManyField(Tag, verbose_name='标签')

    objects = ArticleManager()

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']

    def __unicode__(self):
        return self.title

#评论模型
class Comment(models.Model):
    content = models.TextField(verbose_name= '评论内容')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name= '发布时间' )
    user = models.ForeignKey(User,blank= True,null= True,verbose_name= '用户')
    article = models.ForeignKey(Article,blank= True,null= True, verbose_name= '文章')
    pid = models.ForeignKey('self',blank= True,null= True, verbose_name='父级评论')

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']

    def __unicode__(self):
        return str(self.id)

#友情链接
class Links(models.Model):
    title = models.CharField(max_length= 50,verbose_name= '标题')
    description = models.CharField(max_length= 200,verbose_name= '友情链接描述')
    callback_url = models.URLField(verbose_name= 'url地址')
    date_publish = models.DateTimeField(auto_now_add=True, verbose_name= '发布时间' )
    index = models.IntegerField(default= 999,verbose_name= '排列顺序（从小到大）')

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name
        ordering = ['index','id']

    def __unicode__(self):
        return self.title

#ip
class Ip(models.Model):
    ip = models.CharField(max_length=40)

    class Meta:
        verbose_name = 'IP'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __unicode__(self):
        return self.ip