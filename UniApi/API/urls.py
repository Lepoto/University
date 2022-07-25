from django.urls import path
from API import views

urlpatterns = [
    path('institution/', views.InstitutionAPIView.as_view()),
    path('institution/<str:pk>', views.get_institution),
    path('bursaries/', views.BursaryAPIView.as_view()),
    path('bursaries/<str:pk>', views.get_bursary),
    path('courses/', views.CourseAPIView.as_view()),
    path('courses/<str:pk>', views.get_course)
]