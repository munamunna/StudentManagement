from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView
from student.models import Student
from .forms import StudentForm,StudentChangeForm
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.
class IndexView(ListView):
    template_name="index.html"
    model=Student
    context_object_name="students"

class StudentDetail(DetailView):
    template_name="index.html"
    model=Student
    context_object_name="student"

class CreateStudent(CreateView):
    form_class=StudentForm
    model=Student
    template_name="student-add.html"
    success_url=reverse_lazy("student-add")

    def form_valid(self, form):
        
        
        messages.success(self.request,"student has been created")
        return super().form_valid(form)

class StudentEditView(UpdateView):
        model=Student
        form_class=StudentChangeForm
        template_name="student-edit.html"
        success_url=reverse_lazy("student-edit")

        def form_valid(self, form):
            messages.success(self.request,"changed")
            return super().form_valid(form)
        
def student_delete_view(request,*args,**kargs):
    id=kargs.get("pk")
    Student.objects.get(id=id).delete()
    messages.success(request,"task removed")
    return redirect("index")
     