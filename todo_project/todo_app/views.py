from django.shortcuts import render, redirect

from .forms import TodoForm
from .models import Task


# Create your views here.
def home(request):
    task1=Task.objects.all()
    if request.method=='POST':
        title=request.POST.get('title','')
        priority = request.POST.get('priority', '')
        date=request.POST.get('date','')
        task=Task(title=title,priority=priority,date=date)
        task.save();

    return render(request,'home.html',{'task_new': task1})
def delete(request,id):
    task1 = Task.objects.get(id=id)
    if request.method=='POST':
        task1.delete()
        return redirect('/')
    return render(request,'delete.html')
def edit(request,id):
    task1=Task.objects.get(id=id)
    frm_new=TodoForm(request.POST or None ,instance=task1)
    if frm_new.is_valid():
        frm_new.save()
        return redirect('/')
    return render(request,'edit.html',{'frm':frm_new,'tsk':task1})










