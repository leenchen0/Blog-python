from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from articles.models import Article, Article_sort, Article_tag, TagToArt, comment, UserProfile
from django.contrib.auth.models import User
from django.db.models import Count
from django.contrib.auth import authenticate, login, logout

import urllib
import json
import re

#type==1,category;type==2, tags;type==3, content;
def GetArticle(type, keywords):
    remove_count = 0
    keywords = keywords.split(' ')
    for x in xrange(0,len(keywords)):
        t = x-remove_count
        if t>0 and keywords[t] == '' and keywords[t-1] != '':
            keywords[t-1] += '+'
            keywords.remove(keywords[t])
            remove_count += 1
    #type!=3
    if type!="3":
        temp = []
        if type=="1":    
            for keyword in keywords:
                if temp==[]:
                    temp = Article_sort.objects.filter(article_type = keyword).order_by('-id')
                else:
                    temp = temp | Article_sort.objects.filter(article_type = keyword).order_by('-id')
        if type=="2":
            for keyword in keywords:
                tag_obj = Article_tag.objects.filter(Tag_name = keyword)
                if len(tag_obj)>0:
                    tag_obj = tag_obj[0]
                    if temp==[]:
                        temp = TagToArt.objects.filter(tag_id = tag_obj).order_by('-id')
                    else:
                        temp = temp | TagToArt.objects.filter(tag_id = tag_obj).order_by('-id')
        article = []
        for x in temp:
            if x.article_id.state==0:
                article.append(x.article_id)
        return article

    #type==3
    if type=="3":
        for keyword in keywords:
            temp = []
            if temp==[]:
                temp = Article.objects.filter(state = 0).filter(content__contains=keyword).order_by('-date')
            else:
                temp = temp | Article.objects.filter(state = 0).filter(content__contains=keyword).order_by('-date')
        return temp

def getList():
    sort_type_list = Article_sort.objects.values('article_type').annotate(dcount=Count('article_type'))
    category = []
    for sort_type in sort_type_list:
        category.append({"dcount":sort_type['dcount'],"sort_name":sort_type["article_type"]})
        # category.append({"dcount":sort_type['dcount'], "id":Article_sort.objects.filter(article_type = sort_type["article_type"])[0].id,"sort_name":sort_type["article_type"], "articles":Article_sort.objects.filter(article_type = sort_type["article_type"])})
    return category

def ListRet( article, request):
    category = getList()
    tags = Article_tag.objects.all()
    return render(request, 'articles.html',{"Article":article,"category":category, "tags":tags})

def List():
    article = Article.objects.all().filter(state = 0).order_by('-date')
    return article

def Detail ( request, article_id ):
    code = request.GET.get("code", "none")
    head_img = '/resource/static/images/logo.png'
    state = 0
    open_id = ''
    user_name = ''
    msg = 0
    if code!="none":
        state = 1
        #Get access_token
        params = urllib.urlencode({'grant_type':'authorization_code', 'client_id': '101337112', 'client_secret':'52fe9aa44324d28c3e14c0678ba6e8d0', 'code': code, 'state': '[The_CLIENT_STATE]', 'redirect_uri':'http://pencilsky.cn/articles/32/'})
        f = urllib.urlopen("https://graph.qq.com/oauth2.0/token?%s" % params)
        result = f.read()
        if result.find('access_token=')!=-1:
            access_token = result[result.find('access_token=')+13:result.find('&')]
            #Get open_id
            params = urllib.urlencode({'access_token':access_token})
            f = urllib.urlopen("https://graph.qq.com/oauth2.0/me?%s" % params)
            result = f.read()
            if result.find('"openid":"')!=-1:
                open_id = result[result.find('"openid":"')+10:result.find('"} );')]
                #Get user_info
                params = urllib.urlencode({'access_token':access_token, 'oauth_consumer_key':'101337112', 'openid': open_id})
                f = urllib.urlopen("https://graph.qq.com/user/get_user_info?%s" % params)
                result = json.loads(f.read())
                if result.has_key('figureurl_qq_1'):
                    #Get head_img
                    head_img = result['figureurl_qq_1']
                    user_name = result.get('nickname', 'Pencil')
                    user = User.objects.filter(username=open_id)
                    if len(user)==0:#new user need to be created
                        user = User()
                        user.username = open_id
                        user.set_password("pencilsky.cn")
                        user.email = ''
                        user.save()
                        profile = UserProfile()
                        profile.user = user
                        profile.HeadImg = head_img
                        profile.Name = user_name
                        profile.save()
                    else:#exist then update the user's info
                        user = user[0]
                        profile = user.userprofile
                        profile.HeadImg = head_img
                        profile.Name = user_name
                        profile.save()

                    newUser = authenticate(username=open_id,password="pencilsky.cn")
                    if newUser is not None:
                        login(request, newUser)
                        return HttpResponseRedirect('http://pencilsky.cn/articles/'+article_id+'/')
                    else:
                        msg = 4
                else :
                    msg = 3
            else:
                msg = 2
        else:
            msg = 1
    else:
        if request.user.is_authenticated():
            try:
                profile = request.user.userprofile
                head_img = profile.HeadImg
                user_name = profile.Name
                open_id = request.user.username
            except :
                logout(request)
            


    article = Article.objects.filter(state = 0).filter(article_id=article_id)
    article_tags = []
    if len(article)>0:
        article = article[0]
        
        temp = TagToArt.objects.filter(article_id = article)
        for x in temp:
            article_tags.append(x.tag_id.Tag_name)
        temp = Article_sort.objects.filter(article_id = article)
        if len(temp)>0:
            article.sort = temp[0].article_type
    else:
        return render(request, 'error_info.html', {'msg': 9, 'next_url': 'http://pencilsky.cn/articles/'})

    article_last = Article.objects.filter(state = 0).filter(article_id__lt=article_id).order_by('-article_id')
    if len(article_last)>0:
        article_last = article_last[0]
        article_last = {
            'id' : article_last.article_id,
            'title' : article_last.title
        }
    else:
        article_last = {
            'id': -1,
            'title' : "NULL"
        }
    
    article_next = Article.objects.filter(state = 0).filter(article_id__gt=article_id).order_by('article_id')
    if len(article_next)>0:
        article_next = article_next[0]
        article_next = {
            'id' : article_next.article_id,
            'title' : article_next.title
        }
    else:
        article_next = {
            'id' : -1,
            'title' : "NULL"
        }

    category = getList()
    tags = getTags()
    if state==1 and msg!=0:
        return render(request, 'error_info.html', {'msg': msg, 'next_url': 'http://pencilsky.cn/articles/'+article_id+'/'})
    comnt = getComment(article_id)
    return render(request, 'article_detail.html', {'article_last': article_last, 'article_next': article_next, 'comment': comnt, 'open_id': open_id, 'now_url': 'http://pencilsky.cn/articles/'+article_id+'/', 'head_img': head_img, 'user_name': user_name, "Article":article,"tags":tags,"article_tags":article_tags,"category":category})

def Logout( request ):
    next_url = request.GET.get('redirect', 'NULL')
    if next_url!='NULL':
        logout(request)
        return HttpResponseRedirect(next_url)
    next_url = request.GET.get('url', 'NULL')
    if next_url!='NULL':
        code = request.GET.get('code', '')
        return HttpResponseRedirect(next_url+'?code='+code)
    return HttpResponseRedirect('/')

def Search ( request ):
    return ListRet(getSearch( request ), request)

def getTags():
    return Article_tag.objects.all()

def getSearch ( request ):
    keywords = request.GET.get('keywords','')
    type = request.GET.get('type','4')
    if type!="4":
        article = GetArticle(type,keywords)
        return article
    article = GetArticle("1", keywords)
    article.extend(GetArticle("2", keywords))
    article.extend(GetArticle("3", keywords))
    article = list(set(article))
    return article

def getComment ( article_id ):
    result = {
        'sum':0,
        'content':[]
    }
    result_parent = comment.objects.filter(article_id = article_id).filter(last_id=-1)
    result['sum'] = len(result_parent)
    for i in result_parent:
        last_id = i.id
        result_child = comment.objects.filter(last_id=last_id)
        result['sum'] = result['sum'] + len(result_child)
        result_tmp = []
        result_tmp.append(i)
        for x in result_child:
            result_tmp.append(x)
        result['content'].append(result_tmp)
    return result

def comment_create( request, article_id):
    if request.method=="POST":
        com_met = request.POST.get('login', '0')
        if com_met=='0' or com_met=='1':
            if com_met=='0':
                open_id = request.POST.get('openid', 'NULL')
                user = User.objects.filter(username=open_id)
                if len(user)>0:
                    user = user[0]
                else:
                    return render(request, 'error_info.html', {'msg': 5, 'next_url': 'http://pencilsky.cn/articles/'+article_id+'/'})
                    # "Please login first, and then commenting or commenting as a visitor"
            else:
                user_name = request.POST.get('name', 'NULL')[:40]
                user_portrait = request.POST.get('head_img_url', '/static/images/logo.png')
                email = request.POST.get('email', '')
                user = User.objects.filter(username="visitor:"+user_name)
                if len(user)==0:
                    user = User()
                    user.username = "visitor:"+user_name
                    user.set_password("pencilsky.cn")
                    user.email = email
                    user.save()
                    profile = UserProfile()
                    profile.user = user
                    profile.HeadImg = user_portrait
                    profile.Name = user_name
                    profile.save()
                else:
                    user = user[0]

            if request.POST.get('rid', '')=='':
                last_id = -1;
            else:
                last_id = int(request.POST.get('rid', '-1'))
            
            if last_id!=-1:
                tmp = comment.objects.filter(id=last_id).filter(article_id = article_id)
                if len(tmp)==0:
                    return render(request, 'error_info.html', {'msg': 8, 'next_url': 'http://pencilsky.cn/articles/'+article_id+'/'})

            content = request.POST.get('content', '')
            # replace harmful content
            pattern = ["(?i)<(/?)(script|i?frame|style|html|body|title|link|meta)>", "(?i)(<[^>]*)on[a-za-z]+s*=([^>]*>)"]
            newstring = ["", "12"]
            for i in range(0, len(pattern)):
                if re.search(pattern[i], content):
                    content = re.subn(pattern[i], newstring[i], content)

            ip = request.POST.get('ip', '');
            isp = request.POST.get('isp', '');
            browser = request.POST.get('browser', '');
            os = request.POST.get('os', '');

            article = Article.objects.filter(state = 0).filter(article_id=article_id)
            if len(article)>0:
                comment.objects.create(user=user, article_id = article_id, last_id = last_id, content = content, user_ip = ip, user_isp = isp, user_browser = browser, user_os = os)
            else:
                return render(request, 'error_info.html', {'msg': 7, 'next_url': 'http://pencilsky.cn/articles/'})

        else:
            return render(request, 'error_info.html', {'msg': 6, 'next_url': 'http://pencilsky.cn/articles/'+article_id+'/'})

    return HttpResponseRedirect(request.POST.get('next_url', '/'))
