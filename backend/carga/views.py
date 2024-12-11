from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated

class UniversitiesViewSet(ModelViewSet):
    queryset = Universities.objects.all()
    serializer_class = UniversitiesSerializer
    permission_classes = [IsAuthenticated]

class FacultiesViewSet(ModelViewSet):
    queryset = Faculties.objects.all()
    serializer_class = FacultiesSerializer
    permission_classes = [IsAuthenticated]

class DepartmentsViewSet(ModelViewSet):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer
    permission_classes = [IsAuthenticated]

class AreasViewSet(ModelViewSet):
    queryset = Areas.objects.all()
    serializer_class = AreasSerializer
    permission_classes = [IsAuthenticated]

class CareersViewSet(ModelViewSet):
    queryset = Careers.objects.all()
    serializer_class = CareersSerializer
    permission_classes = [IsAuthenticated]

class CurriculumsViewSet(ModelViewSet):
    queryset = Curriculums.objects.all()
    serializer_class = CurriculumsSerializer
    permission_classes = [IsAuthenticated]

class CoursePrerequisitesViewSet(ModelViewSet):
    queryset = CoursePrerequisites.objects.all()
    serializer_class = CoursePrerequisitesSerializer
    permission_classes = [IsAuthenticated]

class CoursesViewSet(ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    permission_classes = [IsAuthenticated]

class ProfessorsViewSet(ModelViewSet):
    queryset = Professors.objects.all()
    serializer_class = ProfessorsSerializer
    permission_classes = [IsAuthenticated]

class GroupsViewSet(ModelViewSet):
    queryset = Groups.objects.all()
    serializer_class = GroupsSerializer
    permission_classes = [IsAuthenticated]

class CourseLoadsViewSet(ModelViewSet):
    queryset = CourseLoads.objects.all()
    serializer_class = CourseLoadsSerializer
    permission_classes = [IsAuthenticated]

class SemestersViewSet(ModelViewSet):
    queryset = Semesters.objects.all()
    serializer_class = SemestersSerializer
    permission_classes = [IsAuthenticated]

class AcademicDegreesViewSet(ModelViewSet):
    queryset = AcademicDegrees.objects.all()
    serializer_class = AcademicDegreesSerializer
    permission_classes = [IsAuthenticated]

class AcademicSemestersViewSet(ModelViewSet):
    queryset = AcademicSemesters.objects.all()
    serializer_class = AcademicSemestersSerializer
    permission_classes = [IsAuthenticated]

class UsersViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [IsAuthenticated]

class StudentsViewSet(ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    permission_classes = [IsAuthenticated]

class ProfessionsViewSet(ModelViewSet):
    queryset = Professions.objects.all()
    serializer_class = ProfessionsSerializer
    permission_classes = [IsAuthenticated]

