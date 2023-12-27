from django.db import models

# Create your models here.
class BaseModel(models.Model): 
    created_at = models.DateTimeField(auto_now_add=True, db_index=True) 
    updated_at = models.DateTimeField(auto_now=True) 

    class Meta: 
        abstract = True
        
class Block(BaseModel):
    year = models.IntegerField()
    block = models.CharField(max_length=10)
    
    @property
    def name(self):
        return f"BSCS{self.year} B{self.block}"
    
    def __str__(self):
        return self.name
    
class Student(BaseModel):
    student_number = models.CharField(max_length=9)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    contact_number = models.CharField(max_length=15, null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    block = models.ForeignKey(Block, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='student_images/', null=True, blank=True)
    
    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name}"
    
    def __str__(self):
        return self.full_name
    
class Teacher(BaseModel):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    contact_number = models.CharField(max_length=15, null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    courses = models.ManyToManyField('Course')
    
    @property
    def full_name(self):
        return f"{self.last_name} {self.first_name}"
    
    def __str__(self):
        return self.full_name
    
class Course(BaseModel):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    prerequisites = models.ManyToManyField('self', symmetrical=False, blank=True, verbose_name="Prerequisite Courses",)
    
    def __str__(self):
        return self.name
    
    def clean(self):
        self.prerequisites = self.prerequisites.exclude(pk=self.pk)

class Class(BaseModel):
    block = models.ForeignKey(Block, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
    @property
    def name(self):
        return f"{self.course} - {self.block}"
    
    def __str__(self):
        return self.name




