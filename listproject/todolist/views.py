from django.shortcuts import render, redirect
from .models import Todolist

def home(request):
    todolist= Todolist.objects.all().order_by('duedate')
    return render(request,'home.html',{'todolist':todolist})

def new(request):
    if request.method=='POST':
     new_list= Todolist.objects.create(
         title=request.POST['title'],
         content=request.POST['content'],
         duedate=request.POST['duedate']
     )
     return redirect('detail',post_pk=new_list.pk)
    else:
     return render(request,'new.html')

def detail(request, post_pk):
    chosen_list= Todolist.objects.get(pk= post_pk)
    return render (request, 'detail.html',{'chosen_list':chosen_list})

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
    

    




# Create your views here.
