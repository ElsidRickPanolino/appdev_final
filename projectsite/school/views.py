from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from school.models import Student, Teacher, Course, Block, Class
from school.forms import StudentForm, TeacherForm, CourseForm, BlockForm, ClassForm

from django.urls import reverse_lazy

# Create your views here.

# READ

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
    paginate_by = 3

class StudentByBlockList(ListView):
    model = Block
    template_name = 'students_by_block.html'
    context_object_name = 'blocks'

    def get_queryset(self):
        return Block.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blocks = context['blocks']
        students_by_block = {}

        for block in blocks:
            students = Student.objects.filter(block=block)
            students_by_block[block] = students

        context['students_by_block'] = students_by_block
        return context


class TeacherList(ListView):
    model = Teacher
    context_object_name = 'teachers'
    template_name = 'teachers.html'
    paginate_by = 5

class TeacherByCourseList(ListView):
    template_name = 'teachers_course.html'
    context_object_name = 'teachers'

    def get_queryset(self):
        return Teacher.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        teachers = context['teachers']
        courses_by_teacher = {}

        for teacher in teachers:
            courses_by_teacher[teacher] = teacher.courses.all()

        context['courses_by_teacher'] = courses_by_teacher
        return context
    
class CourseList(ListView):
    model = Course
    context_object_name = 'courses'
    template_name = 'courses.html'
    paginate_by = 5
    
class CourseWithTeachersList(ListView):
    template_name = 'courses_teachers.html'
    context_object_name = 'courses'

    def get_queryset(self):
        return Course.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        courses = context['courses']
        teachers_by_course = {}

        for course in courses:
            teachers_by_course[course] = course.teacher_set.all()

        context['teachers_by_course'] = teachers_by_course
        return context
    
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
    
    
# CREATE

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'add.html'
    success_url = reverse_lazy('student-list')
    
class TeacherCreateView(CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'add.html'
    success_url = reverse_lazy('teacher-list')
    
class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'add.html'
    success_url = reverse_lazy('course-list')
    
class BlockCreateView(CreateView):
    model = Block
    form_class = BlockForm
    template_name = 'add.html'
    success_url = reverse_lazy('block-list')
    
    
class ClassCreateView(CreateView):
    model = Class
    form_class = ClassForm
    template_name = 'add.html'
    success_url = reverse_lazy('class-list')
    
# UPDATE
    
class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'edit.html'
    success_url = reverse_lazy('student-list')
    
    
class TeacherUpdateView(UpdateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'edit.html'
    success_url = reverse_lazy('teacher-list')
    
class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'edit.html'
    success_url = reverse_lazy('course-list')
    
class BlockUpdateView(UpdateView):
    model = Block
    form_class = BlockForm
    template_name = 'edit.html'
    success_url = reverse_lazy('block-list')
    
class ClassUpdateView(UpdateView):
    model = Class
    form_class = ClassForm
    template_name = 'edit.html'
    success_url = reverse_lazy('class-list')
    
    
# DELETE

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'del.html'
    success_url = reverse_lazy('student-list')
    

class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = 'del.html'
    success_url = reverse_lazy('teacher-list')
    

class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'del.html'
    success_url = reverse_lazy('course-list')
    

class BlockDeleteView(DeleteView):
    model = Block
    template_name = 'del.html'
    success_url = reverse_lazy('block-list')
    

class ClassDeleteView(DeleteView):
    model = Class
    template_name = 'del.html'
    success_url = reverse_lazy('class-list')