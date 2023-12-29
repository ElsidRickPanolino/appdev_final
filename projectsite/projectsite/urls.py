"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from school.views import HomePageView, StudentList, TeacherList, CourseList, BlockList, ClassList
from school.views import StudentByBlockList, TeacherByCourseList, CourseWithTeachersList
from school.views import StudentCreateView, TeacherCreateView, CourseCreateView, BlockCreateView, ClassCreateView
from school.views import StudentUpdateView, TeacherUpdateView, CourseUpdateView, BlockUpdateView, ClassUpdateView
from school.views import StudentDeleteView, TeacherDeleteView, CourseDeleteView, BlockDeleteView, ClassDeleteView
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('student_list', StudentList.as_view(), name='student-list'),
    path('students/by_block/', StudentByBlockList.as_view(), name='student-by-block'),
    path('teacher_list', TeacherList.as_view(), name='teacher-list'),
    path('teachers/by_course/', TeacherByCourseList.as_view(), name='teacher-by-course'),
    path('course_list', CourseList.as_view(), name='course-list'),
    path('courses/with_teachers/', CourseWithTeachersList.as_view(), name='courses-with-teachers'),
    path('block_list', BlockList.as_view(), name='block-list'),
    path('class_list', ClassList.as_view(), name='class-list'),
    
    path('student_list/add', StudentCreateView.as_view(), name='student-add'),
    path('teacher_list/add', TeacherCreateView.as_view(), name='teacher-add'),
    path('course_list/add', CourseCreateView.as_view(), name='course-add'),
    path('block_list/add', BlockCreateView.as_view(), name='block-add'),
    path('class_list/add', ClassCreateView.as_view(), name='class-add'),
    
    path('student_list/<pk>', StudentUpdateView.as_view(), name='student-update'),
    path('teacher_list/<pk>', TeacherUpdateView.as_view(), name='teacher-update'),
    path('course_list/<pk>', CourseUpdateView.as_view(), name='course-update'),
    path('block_list/<pk>', BlockUpdateView.as_view(), name='block-update'),
    path('class_list/<pk>', ClassUpdateView.as_view(), name='class-update'),
    
    path('student_list/<pk>', StudentUpdateView.as_view(), name='student-update'),
    path('teacher_list/<pk>', TeacherUpdateView.as_view(), name='teacher-update'),
    path('course_list/<pk>', CourseUpdateView.as_view(), name='course-update'),
    path('block_list/<pk>', BlockUpdateView.as_view(), name='block-update'),
    path('class_list/<pk>', ClassUpdateView.as_view(), name='class-update'),
    
    path('student_list/<pk>/delete', StudentDeleteView.as_view(), name='student-delete'),
    path('teacher_list/<pk>/delete', TeacherDeleteView.as_view(), name='teacher-delete'),
    path('course_list/<pk>/delete', CourseDeleteView.as_view(), name='course-delete'),
    path('block_list/<pk>/delete', BlockDeleteView.as_view(), name='block-delete'),
    path('class_list/<pk>/delete', ClassDeleteView.as_view(), name='class-delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    