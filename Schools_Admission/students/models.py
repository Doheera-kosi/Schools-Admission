# students/models.py
from django.db import models  # type: ignore
import re
from django.core.exceptions import ValidationError  # type: ignore
from django.db.models.signals import post_save  # type: ignore
from django.dispatch import receiver  # type: ignore
from classes.models import Class
from courses.models import Course

# Create your models here.
class Student(models.Model):
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
    )

    RESIDENTIAL_STATUS_CHOICES = (
        ("BOARDING", "Boarding"),
        ("DAY", "Day"),
    )

    JHS_TYPE_CHOICES = (
        ("PRIVATE", "Private"),
        ("PUBLIC", "Public"),
    )

    INTEREST_CHOICES = (
        ("DEBATING CLUB", "Debating Club"),
        ("ARTHLETICS", "Arthletics"),
        ("FOOTBALL", "Football"),
        ("OTHERS", "others"),
    )

    REGION_CHOICES = (
        ("ASHANTI", "Ashanti"),
        ("BONO", "Bono"),
        ("BONO EAST", "Bono East"),
        ("AHAFO", "Ahafo"),
        ("CENTRAL", "Central"),
        ("EASTERN", "Eastern"),
        ("GREATER ACCRA", "Greater Accra"),
        ("NORTHERN", "Northern"),
        ("SAVANNAH", "Savannah"),
        ("NORTH EAST", "North East"),
        ("UPPER EAST", "Upper East"),
        ("VOLTA", "Volta"),
        ("OTI", "Oti"),
        ("WESTERN", "Western"),
        ("WESTERN NORT", "Western Nort"),
    )

    OCCUPATION_CHOICES = (
        ("CROP FARMING", "Crop Farming"),
        ("TRADING", "Trading"),
        ("CHARCOAL PRODUCTION", "Charcoal Production"),
        ("ANIMALS FARMING", "Animals Farming"),
        ("HUNTING", "Hunting"),
        ("TEACHING", "Teaching"),
        ("DOCTOR", "Doctor"),
        ("NURSE", "Nurse"),
    )

    RELIGION_CHOICES = (
        ("CHRISTIAN", "Christian"),
        ("MUSLIM", "Muslim"),
        ("TRADITIONALIST", "Traditionalist"),
    )

    RELIGIOUS_DENOM_CHOICES = (
        ("BAPTIST", "Baptist"),
        ("PENTECOST", "Pentecost"),
        ("METHODIST", "Methodist"),
        ("PRESBY", "Presby"),
        ("ASSEMBLES OF GOD", "Assembles of God"),
        ("CATHOLIC", "Catholic"),
        ("ANGLICAN", "Anglican"),
    )

    TOWN_CHOICES = (
        ("WALEWALE", "Walewale"),
        ("TAMALE", "Tamale"),
        ("ACCRA", "Accra"),
        ("TECHIMAN", "Techiman"),
        ("KUMASI", "Kumasi"),
        ("HO", "Ho"),
        ("JEMA", "Jema"),
    )

    DISTRICT_CHOICES = (
        ("WALEWALE WEST", "Welewale West"),
        ("TAMALE WEST", "Tamale West"),
        ("TECHIMAN WEST", "Techiman West"),
    )

    PROGRAMME_CHOICES = (
        ("GENERAL SCIENCE", "General Science"),
        ("GENERAL AGRIC", "General AGRIC"),
        ("GENERAL ARTS", "General Arts"),
        ("HOME ECONOMICS", "Home Economics"),
        ("VISUAL ARTS", "Visual Arts"),
        ("BUSINESS", "Business"),
    )

    # CLASS_NAME_CHOICES = Class.CLASS_NAME_CHOICES
    def validate_decimal_number(value):
        # Regular expression to match a valid decimal number
        if not re.match(r"^\d+(\.\d+)?$", str(value)):
            raise ValidationError("Enter a valid decimal number.")

    def validate_non_negative(value):
        if value < 0:
            raise ValidationError("This field does not accept negative values.")

        # Basic student information

    index_number = models.CharField(max_length=20, unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    school = models.ForeignKey(
        "schools.School", on_delete=models.CASCADE, related_name="students"
    )
    programme = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="students"
    )
    surname = models.CharField(max_length=255)
    other_names = models.CharField(max_length=255)
    aggregate_of_best_six = models.DecimalField(max_digits=5, decimal_places=2)
    raw_score = models.PositiveIntegerField(
        validators=[validate_non_negative], null=True, blank=True
    )

    # Enrollment details
    enrolment_code = models.CharField(max_length=20, null=False, blank=False)
    enrolment_form_image = models.ImageField(
        upload_to="enrolment_forms/", null=True, blank=True
    )

    # Personal details
    date_of_birth = models.DateField(blank=False, null=False)
    place_of_birth = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255, blank=False, null=False)
    religion = models.CharField(max_length=255, choices=RELIGION_CHOICES)
    religious_denomination = models.CharField(
        max_length=255, blank=True, choices=RELIGIOUS_DENOM_CHOICES
    )
    permanent_address = models.CharField(max_length=255)
    town = models.CharField(max_length=255, choices=TOWN_CHOICES)
    region = models.CharField(max_length=255, choices=REGION_CHOICES)
    district = models.CharField(max_length=255, choices=DISTRICT_CHOICES)
    interests = models.TextField(max_length=255, blank=True, choices=INTEREST_CHOICES)
    ghana_card_or_nhis_number = models.CharField(max_length=20)

    # Parental details
    father_name = models.CharField(max_length=255, blank=False, null=False)
    father_occupation = models.CharField(max_length=255, choices=OCCUPATION_CHOICES)
    mother_name = models.CharField(max_length=255)
    mother_occupation = models.CharField(max_length=255, choices=OCCUPATION_CHOICES)
    guardian_name = models.CharField(max_length=255, blank=False)
    residential_telephone = models.CharField(max_length=20, blank=False)
    guardian_digital_address = models.CharField(max_length=255, blank=True)

    # Class selection
    # class_name = models.ForeignKey(
    #     Class, on_delete=models.CASCADE, related_name="students"
    # )

    class_selected = models.ForeignKey(
        Class,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="students",
    )

    # Contact information
    mobile_phone = models.CharField(max_length=20)
    whatsapp_number = models.CharField(max_length=20, blank=True)
    other_phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    # Admission details
    admitted_by = models.ForeignKey(
        'schools.School', on_delete=models.CASCADE, default=1
    )

    def __str__(self):
        return f"{self.index_number} - {self.surname}, {self.other_names}"