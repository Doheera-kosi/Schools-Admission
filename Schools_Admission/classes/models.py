from django.db import models #type: ignore
from schools.models import School
from courses.models import Course

# Create your models here.
class Class(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='classes')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='classes', default=1)
    class_name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField(default=100)

    def __str__(self):
        return f"{self.school.name} - {self.class_name}"