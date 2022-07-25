from django.contrib import admin
from django.utils.html import format_html

from career.models import *
from career.adminDisplay import BursaryAdmin, InstitutionAdmin, FacultyAdmin, SchoolAdmin, CourseAdmin


# Register your models here.
# username = alfred, password = mas@12345

admin.site.register(Institution, InstitutionAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Bursary, BursaryAdmin)
