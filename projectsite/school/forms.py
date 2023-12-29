from django.forms import ModelForm
from django import forms
from .models import Student, Teacher, Block, Course, Class

class StudentForm(ModelForm):
    birthdate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Student
        fields = "__all__"
        
        
class TeacherForm(ModelForm):
    # courses = forms.ModelMultipleChoiceField(
    #     queryset=Course.objects.all(),
    #     widget=forms.CheckboxSelectMultiple,
    #     required=False
    # )

    class Meta:
        model = Teacher
        fields = "__all__"
        
class BlockForm(ModelForm):
    class Meta:
        model = Block
        fields = "__all__"
        
class CourseForm(forms.ModelForm):
    # prerequisites = forms.ModelMultipleChoiceField(
    #     queryset=Course.objects.all(),
    #     widget=forms.CheckboxSelectMultiple,
    #     required=False
    # )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance:
            self.fields['prerequisites'].queryset = Course.objects.exclude(pk=instance.pk)

    class Meta:
        model = Course
        fields = "__all__"
        
        
class ClassForm(ModelForm):
    class Meta:
        model = Class
        fields = "__all__"