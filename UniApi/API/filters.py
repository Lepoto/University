import django_filters
from django_filters import filters
from career.models import Bursary


class BursaryFilter(django_filters.FilterSet):
    class Meta:
        model = Bursary
        fields = ['bursary_name', 'bursary_field_study_1']
