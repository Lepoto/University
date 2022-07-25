from rest_framework import serializers
from career.models import Institution, Faculty, Bursary, School, Course


class InstitutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institution
        fields = '__all__'

        """Serializing universities"""


class FacultiesSerializer(serializers.ModelSerializer):
    institution = InstitutionSerializer()

    class Meta:
        model = Faculty
        fields = '__all__'

        """Serializing all faculties"""

class SchoolSerializer(serializers.ModelSerializer):
    school_faculty = FacultiesSerializer()

    class Meta:
        model = School
        fields = '__all__'

        """Serializing all schools in their respective faculty"""

class CourseSerializer(serializers.ModelSerializer):
    school_name = SchoolSerializer()

    class Meta:
        model = Course
        fields = '__all__'

        """Serializing all courses in their respective schools"""

class BursarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Bursary
        fields = '__all__'

        """Serializing all faculties"""
