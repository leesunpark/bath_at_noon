
from datetime import time
from django.shortcuts import get_object_or_404, render, redirect
from newscomments.models import Comment
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from newscomments.forms import CommentForm

def index(request):

    num_comments = 75 + Comment.objects.all().count()
    comment = [
        item.to_json() for item in Comment.objects.all().order_by('-id')]
    
    context = {
        'comments': comment,
        'num_comments' : num_comments,
    }
  
    return render(request, 'index.html', context=context)


def add_comment(request):

    if "POST" != request.method:
        raise HttpResponse(status=404)
    if "POST" == request.method:
        name = request.POST.get("new_name")
        content = request.POST.get("new_content")
        
        if not name:
            return HttpResponse('아이디를 입력해주세요.') 
            
        if not content:
            return HttpResponse('댓글을 입력해주세요.')
        
        if name and content:
            comment_instance = Comment(name=name, content=content, date=timezone.now())
            comment_instance.save() 
            return redirect('index')