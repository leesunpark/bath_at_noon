
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
            return HttpResponse('Invalid name')
        if not content:
            return HttpResponse('Invalid content')
        comment_instance = Comment(name=name, content=content, date=timezone.now())
        comment_instance.save() 

    context ={
        'comment_instance' : comment_instance,
    }
        
    
    return redirect('index')

    '''
    comment_instance =get_object_or_404(Comment)
    
    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment_instance.name = form.cleaned_data['new_name']
            comment_instance.content = form.cleaned_data['new_content']
            comment_instance.save()
            return HttpResponseRedirect(reverse(''))
        
    context = {
        'form' : form,
        'comment_instance' : comment_instance,
    }

    return render(request, 'index.html', context)
    '''

    '''
    if "POST" != request.method:
        raise HttpResponse(status=404)
    name = request.POST.get("name", None)
    content = request.POST.get("content", None)
    if not name:
        return HttpResponse('Invalid name')
    if not content:
        return HttpResponse('Invalid content')
    
    try:
        comment_instance = Comment(name=name, content=content, date=timezone.now())
        comment_instance.save()
    except Exception as e:
        return HttpResponse('Error occured. Try again.')
    return redirect('newscomments:comment_view')
    '''