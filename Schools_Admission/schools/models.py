from django.db import models  # type: ignore


# Create your models here.
class School(models.Model):
    LOCATION_CHOICES = (
        ("KUMASI", "Kumasi"),
        ("TAMALE", "Tamale"),
        ("ACCRA", "Accra"),
        ("TECHIMAN", "Techiman"),
        ("SUNYANI", "Sunyani"),
        ("YENDI", "Yendi"),
        ("SALAGA", "Salaga"),
        ("HO", "Ho"),
        ("KINTAMPO", "Kintampo"),
        ("WALEWALE", "Walewale"),
        ("KOFORIDUA", "Koforidua"),
        ("WA", "Wa"),
    )

    SCHOOL_CHOICES = [
        ("Achimota", "Achimota School"),
        ("Mfantsipim", "Mfantsipim School"),
        ("Adisadel", "Adisadel College"),
        ("St. Augustine's", "St. Augustine's College"),
        ("Prempeh", "Prempeh College"),
        ("Opoku Ware", "Opoku Ware School"),
        ("Wesley Girls'", "Wesley Girls' High School"),
        ("PRESEC", "Presbyterian Boys' Secondary School (PRESEC)"),
        ("St. Peter's", "St. Peter's Senior High School"),
        ("Ghana National", "Ghana National College"),
        ("KETASCO", "Keta Senior High Technical School (KETASCO)"),
        ("Adventist", "Adventist Senior High School"),
        ("St. Louis", "St. Louis Senior High School"),
        ("Tamasco", "Tamale Senior High School (Tamasco)"),
        ("Ghanata", "Ghanata Senior High School"),
        ("St. Mary's", "St. Mary's Senior High School"),
        ("Labone", "Labone Senior High School"),
        ("Achimota SHS", "Achimota Senior High School"),
        ("Pope John", "Pope John Senior High School"),
        ("Adventist Girls'", "Adventist Girls' Senior High School"),
        ("GIS", "Ghana International School"),
        ("Lutheran SHS", "Lutheran Senior High School"),
        ("Alsyd Academy", "Alsyd Academy"),
        ("Galaxy International", "Galaxy International School"),
        (
            "Maranatha University College SHS",
            "Maranatha University College Senior High School",
        ),
        (
            "SOS-Hermann Gmeiner International",
            "SOS-Hermann Gmeiner International College",
        ),
        ("Lincoln Community", "Lincoln Community School"),
        (
            "Regent University College SHS",
            "Regent University College Senior High School",
        ),
        ("Morning Star", "Morning Star School"),
        ("WASS", "West African Secondary School (WASS)"),
    ]

    logo = models.ImageField(upload_to="school_logos/", null=True, blank=True)
    name = models.CharField(
        max_length=100, unique=True, blank=False, null=False, choices=SCHOOL_CHOICES
    )
    location = models.CharField(max_length=100, choices=LOCATION_CHOICES)
    contact_phone = models.CharField(max_length=20, default="+1234567890")
    contact_email = models.EmailField(
        unique=True, max_length=255, null=True, blank=True
    )
    established_year = models.DateField(null=False, max_length=255)
    principal_name = models.CharField(max_length=100, null=True, blank=True)
    principal_contact = models.CharField(
        blank=False, null=False, max_length=20, default="+00-000-000-00"
    )
    administrator_name = models.CharField(max_length=100, null=True, blank=True)
    administrator_contact = models.CharField(
        blank=False, null=False, max_length=20, default="+00-000-000-00"
    )
    max_students = models.PositiveIntegerField(default=0)

    # def __str__(self):
    #     return self.name

    # def remaining_slots(self):
    #     current_students = Student.objects.filter(admitted_by=self).count()
    #     return self.max_students - current_students
