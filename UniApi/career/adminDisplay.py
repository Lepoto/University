from django.utils.html import format_html
from django.contrib import admin


class BursaryAdmin(admin.ModelAdmin):

    def bursary_logo(self, obj):
        return format_html('<img src="{}" style="max-width:100px; max-height:100px" />'.format(obj.bursary_logo.url))

    list_display = ['bursary_name', 'bursary_logo',
                    'bursary_link', 'bursary_added']


class InstitutionAdmin(admin.ModelAdmin):

    def university_logo(self, obj):
        return format_html('<img src="{}" style="max-width:100px; max-height:100px" />'.format(obj.image.url))

    list_display = ['name', 'university_logo', 'status',
                    'link', 'closing' ]


class FacultyAdmin(admin.ModelAdmin):

    def faculty_logo(self, obj):
        return format_html('<img src="{}" style="max-width:100px; max-height:100px" />'.format(obj.image.url))

    list_display = ['institution', 'faculty_name',
                    'faculty_logo', 'email']


class SchoolAdmin(admin.ModelAdmin):
    list_display = ['school_name', 'school_faculty',
                    'school_undergraduate_program']

class CourseAdmin(admin.ModelAdmin):

    list_display = ['school_name', 'course_name',
                    'course_min_aps']
