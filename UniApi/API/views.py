from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import filters, generics, pagination
from API import serializers

from API.serializers import FacultiesSerializer, BursarySerializer, CourseSerializer, InstitutionSerializer

from career.models import Faculty, Bursary, Course, Institution


# GET view for bursaries
class InstitutionAPIView(generics.ListAPIView):
    queryset = Institution.objects.all().order_by('-closing')
    serializer_class = InstitutionSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = {'name'}
    pagination_class = PageNumberPagination

# GET view for a single object
@api_view(['GET'])
def get_institution(request, pk):
    institution = Institution.objects.get(id=pk)
    serializer = InstitutionSerializer(institution, many=False)

    return Response(serializer.data)

# GET view for bursaries
class BursaryAPIView(generics.ListAPIView):
    queryset = Bursary.objects.all().order_by('-bursary_added')
    serializer_class = BursarySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = {'bursary_name', 'bursary_field_study_1'}
    pagination_class = PageNumberPagination

# GET view for a single object
@api_view(['GET'])
def get_bursary(request, pk):
    bursary = Bursary.objects.get(bursary_id=pk)
    serializer = BursarySerializer(bursary, many=False)

    return Response(serializer.data)

# GET View for Courses
class CourseAPIView(generics.ListAPIView):
    queryset = Course.objects.all().order_by('course_name')
    serializer_class = CourseSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = {'course_name'}
    pagination_class = PageNumberPagination

# GET method for a single course
@api_view(['GET'])
def get_course(request, pk):
    course = Course.objects.get(course_id=pk)
    serializer = CourseSerializer(course, many=False)

    return Response(serializer.data)