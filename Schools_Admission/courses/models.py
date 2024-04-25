from django.db import models  # type: ignore


# Create your models here.
class Course(models.Model):
    GENERAL_ARTS = "GENARAL ARTS"
    GENERAL_SCIENCE = "GENERAL SCIENCE"
    BUSINESS = "BUSINESS"
    VISUAL_ARTS = "VISUAL ART"
    HOME_ECONOMICS = "HOME SCIENCE"
    AGRICULTURAL_SCIENCE = "AGRIC SCIENCE"
    TECHNICAL_SKILLS = "TECHNICAL SKILLS"

    COURSE_CHOICES = [
        (GENERAL_ARTS, "General Arts"),
        (GENERAL_SCIENCE, "General Science"),
        (BUSINESS, "Business"),
        (VISUAL_ARTS, "Visual Arts"),
        (HOME_ECONOMICS, "Home Economics"),
        (AGRICULTURAL_SCIENCE, "Agricultural Science"),
        (TECHNICAL_SKILLS, "Technical Skills"),
    ]
    
    YEAR_CHOICES = [
      ('FIRST YEAR', 'First Year'),
      ('SECOND YEAR', 'Second Year'),
      ('THIRD YEAR', 'Third Year'),
    ]

    name = models.CharField(max_length=255, choices=COURSE_CHOICES, unique=True)
    description = models.TextField(blank=True, null=True)
    year = models.CharField(max_length=255, choices=YEAR_CHOICES)
    # code = models.CharField(max_length=20, unique=True)
    # department = models.CharField(max_length=100)
    # semester = models.CharField(max_length=20)
    # instructor = models.CharField(max_length=255)
    # credits = models.DecimalField(max_digits=5, decimal_places=2)
    # prerequisites = models.ManyToManyField('self', blank=True, symmetrical=False)
    
    
    # def save(self, *args, **kwargs):
    #     # Automatically set the name based on the selected course code
    #     if self.code:
    #         # Find the corresponding name from COURSE_CHOICES
    #         self.name = dict(self.COURSE_CHOICES).get(self.code, "")
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"
