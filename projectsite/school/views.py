from django.shortcuts import render

from django.views.generic.list import ListView
from school.models import Student, Teacher, Course, Block, Class

# Create your views here.


class HomePageView(ListView):
    model = Student
    context_object_name = 'home'
    template_name = "base.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    
class StudentList(ListView):
    model = Student
    context_object_name = 'students'
    template_name = 'students.html'
    paginate_by = 5
    
class TeacherList(ListView):
    model = Teacher
    context_object_name = 'teachers'
    template_name = 'teachers.html'
    paginate_by = 5
    
class CourseList(ListView):
    model = Course
    context_object_name = 'courses'
    template_name = 'courses.html'
    paginate_by = 5
    
class BlockList(ListView):
    model = Block
    context_object_name = 'blocks'
    template_name = 'blocks.html'
    paginate_by = 5
    
    
class ClassList(ListView):
    model = Class
    context_object_name = 'classes'
    template_name = 'classes.html'
    paginate_by = 5