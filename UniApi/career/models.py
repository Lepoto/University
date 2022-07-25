from django.db import models
import uuid


# DB table for Institutions
class Institution(models.Model):
    STATUS = (
        ('Open', 'Open'),
        ('Closed', 'Closed'),
    )
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    link = models.CharField(max_length=250, null=True, blank=True)
    image = models.ImageField(default='default.png', upload_to='logo/institutions', null=True, blank=True)
    status = models.CharField(max_length=100, default='Open', choices=STATUS)
    closing = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class Faculty(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
    institution = models.ForeignKey('Institution', on_delete=models.CASCADE)
    faculty_name = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(default='default.png', upload_to='logo/faculties', null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)

    # DB table for faculty per institution

    def __str__(self):
        return self.faculty_name


class School(models.Model):
    school_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    school_name = models.CharField(max_length=100)
    school_faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    school_undergraduate_program = models.FileField(upload_to='pdf/undergraduate', null=True, blank=True)

    def __str__(self):
        return self.school_name


class Course(models.Model):
    course_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    school_name = models.ForeignKey(School, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=100)
    course_duration = models.IntegerField(blank=True, null=True)
    course_description = models.TextField(null=True, blank=True)
    course_requirements = models.TextField(null=True, blank=True)
    course_min_aps = models.IntegerField()

    def __str__(self):
        return self.course_name


class Bursary(models.Model):
    STATUS = (
        ('Open', 'Open'),
        ('Closed', 'Closed'),
    )
    bursary_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    bursary_name = models.CharField(max_length=100)
    bursary_logo = models.ImageField(default='default.png', upload_to='bursaries/', null=True, blank=True)
    bursary_description = models.TextField(null=True, blank=True)
    bursary_field_study_1 = models.TextField(null=True, blank=True)
    bursary_requirements = models.TextField(null=True, blank=True)
    bursary_link = models.CharField(max_length=250)
    bursary_closing_date = models.DateField(blank=True, null=True)
    bursary_added = models.DateTimeField(auto_now_add=True)
    bursary_status = models.CharField(max_length=10, choices=STATUS, default='Open')

    def __str__(self):
        return self.bursary_name

    class Meta:
        ordering = ['bursary_added']
