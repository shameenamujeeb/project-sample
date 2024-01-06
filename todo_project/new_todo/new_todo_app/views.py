from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Task
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView

class TasklistView(ListView):
    model = Task
    template_name = 'home.html'
    context_object_name = 'task_new'
class TaskdetailView(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name ='task2'
class TaskupdateView(UpdateView):
    model=Task
    template_name = 'update.html'
    context_object_name = "task3"
    fields = ('title','priority','date')
    def get_success_url(self):
        return  reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})
class TaskdeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')



def home(request):
    if request.method=='POST':
        title = request.POST.get('title', '')
        priority = request.POST.get('priority', '')
        date=request.POST.get('date','')
        tsk1=Task(title=title,priority=priority,date=date)
        tsk1.save();
    return render(request,'home.html')