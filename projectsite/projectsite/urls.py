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

from school.views import HomePageView, StudentList, TeacherList, CourseList, BlockList, ClassList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('student_list', StudentList.as_view(), name='student-list'),
    path('teacher_list', TeacherList.as_view(), name='teacher-list'),
    path('course_list', CourseList.as_view(), name='course-list'),
    path('block_list', BlockList.as_view(), name='block-list'),
    path('class_list', ClassList.as_view(), name='class-list'),
]
