from django.contrib import admin

from .models import Block, Student, Teacher, Course, Class

# Register your models here.

class StudentInline(admin.TabularInline):
    model = Student
    fields = ("student_number", "last_name", "first_name", "middle_name", "email", "contact_number", "birthdate", "address", "image", "created_at", "updated_at")
    readonly_fields = ("student_number",)  # Add fields you want to display or make read-only

class PrerequisiteInline(admin.TabularInline):
    model = Course.prerequisites.through
    fk_name = 'from_course'
    verbose_name = 'Prerequisite Course'
    verbose_name_plural = 'Prerequisite Courses'

@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ("year", "block", "display_name")
    search_fields = ("display_name",)
    
    def display_name(self, obj):
        return obj.name

    display_name.short_description = 'Name'
    inlines = [StudentInline]
    
    
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_number", "last_name", "first_name", "middle_name", "email", "contact_number", "birthdate", "address","block","image", "created_at", "updated_at")
    search_fields = ("student_number",)


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "middle_name", "email", "contact_number", "birthdate", "address","display_courses", "created_at", "updated_at")
    search_fields = ("last_name","first_name", "email")


    def display_courses(self, obj):
        return ', '.join([course.name for course in obj.courses.all()])

    display_courses.short_description = 'Courses'
    


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "description", "created_at", "updated_at")
    search_fields = ("code", "name")
    inlines = [PrerequisiteInline]


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ("block", "teacher", "course", "created_at", "updated_at")
    search_fields = ("block","course")