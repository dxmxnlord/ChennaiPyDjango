from django.shortcuts import render
from .models import Post,Comment
from django.shortcuts import get_object_or_404,get_list_or_404
import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect

# Create your views here.

def index(request,pageno=1):
    total_posts=Post.objects.all().count()
    total_pages=total_posts/10
    if ( total_posts % 10 == 0 ):
        total_pages -=1
    lower=(pageno-1)*10 
    upper=pageno*10
    if ( pageno == total_pages + 1 ):
        all_posts=Post.objects.all()[lower:]
    else : 
        all_posts=Post.objects.all()[lower:upper-1]
    total_pages+=1
    return render(request,'blog/list.html',{"posts":all_posts,"page_no":pageno,"total_posts":total_posts,"total_pages":total_pages})

def viewpost(request,postid):
    post_to_view=get_object_or_404(Post,pk=postid)
    comments=Comment.objects.filter(post__id=postid)
    return render(request,'blog/view.html',{"post_to_view":post_to_view,"comments":comments})

def createpost(request):
    if request.method == "POST": 
        try :
            post_title=request.POST['title']
            post_content=request.POST['content']
            post_datetime=datetime.datetime.now()
            post_obj=Post.objects.create(title=post_title,date=post_datetime,content=post_content)
            return redirect('blog:viewpost',postid=post_obj.id)
        except KeyError:
            return render(request,'blog/list.html')
        else:
            return render(request,'blog/list.html')
            
def gotocreatepost(request):
    return render(request,'blog/create.html')

def gotoeditpost(request,postid):
    post_to_edit=get_object_or_404(Post,pk=postid)
    return render(request,'blog/edit.html',{"postid":postid,"post_to_edit":post_to_edit})

def editpost(request,postid):
    if request.method == "POST": 
        try:
            post_title=request.POST['title']
            post_content=request.POST['content']
            post_obj=Post.objects.get(pk=postid)
            post_obj.title=post_title
            post_obj.content=post_content
            post_obj.save()
            return redirect('blog:viewpost',postid=postid)
        except KeyError:
            return render(request,'blog/list.html')
        else:
            return render(request,'blog/list.html')

def deletepost(request,postid):
    post_to_delete=get_object_or_404(Post,pk=postid)
    post_to_delete.delete()
    return redirect('blog:index')

def createcomment(request,postid):
    if request.method == "POST":
        try: 
            comment_text=request.POST['text']
            date_time=datetime.datetime.now()
            comment_name=request.POST['name']
            post_obj=get_object_or_404(Post,pk=postid)
            comment_obj=Comment.objects.create(name=comment_name,date=date_time,comment=comment_text,post=post_obj)
            return redirect('blog:viewpost',postid=postid)
        except KeyError:
            return render(request,'blog/list.html')
        else:
            return render(request,'blog/list.html')
