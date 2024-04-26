from django.db import models #type: ignore
from schools.models import School
from courses.models import Course

# Create your models here.
class Class(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='classes')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='classes', default=1)
    class_name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField(default=100)
    
    current_students = models.PositiveIntegerField(default=0)
    
    def is_full(self):
        return self.current_students >= self.capacity
    
    def enroll_student(self):
        if not self.is_full():
            self.current_students += 1
            self.save()
            return True
        return False

    def __str__(self):
        return f"{self.school.name} - {self.class_name}"