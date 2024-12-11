from rest_framework import serializers
from .models import *

class UniversitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Universities
        fields = '__all__'

class FacultiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculties
        fields = '__all__'

class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = '__all__'

class AreasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Areas
        fields = '__all__'

class CareersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Careers
        fields = '__all__'

class CurriculumsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curriculums
        fields = '__all__'

class CoursePrerequisitesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoursePrerequisites
        fields = '__all__'

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'

class ProfessorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professors
        fields = '__all__'

class GroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = '__all__'

class CourseLoadsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseLoads
        fields = '__all__'

class SemestersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semesters
        fields = '__all__'

class AcademicDegreesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicDegrees
        fields = '__all__'

class AcademicSemestersSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcademicSemesters
        fields = '__all__'

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'

class ProfessionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professions
        fields = '__all__'
