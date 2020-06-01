from django.shortcuts import render, redirect
from .models import Todolist, Comment
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def home(request):
    posts= Todolist.objects.all().order_by('duedate')
    return render(request,'home.html',{'posts':posts})

@login_required(login_url = '/registration/login')
def new(request):
    if request.method=='POST':
     new_list= Todolist.objects.create(
         title=request.POST['title'],
         content=request.POST['content'],
         duedate=request.POST['duedate'],
         author = request.user
     )
     return redirect('detail',post_pk=new_list.pk)
    else:
     return render(request,'new.html')

@login_required(login_url = '/registration/login')
def mypage(request):
    posts= Todolist.objects.all()
    return render(request, 'mypage.html', {'posts':posts}) 

def detail(request, post_pk):
    chosen_list= Todolist.objects.get(pk= post_pk)
    if request.method=="POST":
        Comment.objects.create(
            post = chosen_list,
            content = request.POST['content'],
            author= request.user
        )
        return redirect('detail', post_pk)
    return render (request, 'detail.html',{'chosen_list':chosen_list})

def delete_comment(request, post_pk, comment_pk):
    comment= Comment.objects.get(pk= comment_pk)
    comment.delete()
    return redirect('detail', post_pk)

def edit_comment(request, post_pk, comment_pk ):
    comment= Comment.objects.get(pk = comment_pk)
    if request.method=='POST':
        Comment.objects.filter(pk= comment_pk).update(
         content= request.POST['content']
        )
        return redirect ('detail',post_pk)
    return render(request, 'edit_comment.html')

def delete(request, post_pk):
    chosen_list= Todolist.objects.get(pk= post_pk)
    chosen_list.delete()
    return redirect ('home')

def edit(request, post_pk):
    chosen_list = Todolist.objects.get(pk= post_pk)
    if request.method == 'POST':
        Todolist.objects.filter(pk= post_pk).update(
         title= request.POST['title'],
         content= request.POST['content'],
         duedate= request.POST['duedate']
        )
        return redirect('detail', post_pk)
    return render(request, 'edit.html', {'chosen_list': chosen_list})

def signup(request):
    if (request.method == 'POST'):
        found_user = User.objects.filter(username = request.POST['username'] )
        if (len(found_user)>0):
            error = '중복되는 아이디가 존재합니다'
            return render(request, 'registration/signup.html', {'error': error})
        new_user = User.objects.create_user(    
            username = request.POST['username'],
            password = request.POST['password']
        )
        auth.login(request, new_user, backend= 'django.contrib.auth.backends.ModelBackend')
        return redirect('home')        
    return render(request, 'registration/signup.html')

def login(request):
    if request.method == "POST":
        found_user = auth.authenticate(
            username = request.POST['username'],
            password = request.POST['password']
        )
        if found_user is None:
            error = '아이디 또는 비밀번호가 틀렸습니다'
            return render(request, 'registration/login.html', {'error': error})
        auth.login(request, found_user, backend= 'django.contrib.auth.backends.ModelBackend')
        return redirect(request.GET.get('next','/'))
    return render(request, 'registration/login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')







# Create your views here.
