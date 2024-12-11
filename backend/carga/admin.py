from django.contrib import admin

# Register your models here.

from .models import (
    Universities, Faculties, Departments, Areas, Careers, Curriculums, 
    CoursePrerequisites, Courses, Professors, Groups, CourseLoads, 
    Semesters, AcademicDegrees, AcademicSemesters, Users, Students, Professions
)
admin.site.register(Universities)
admin.site.register(Faculties)
admin.site.register(Departments)
admin.site.register(Areas)
admin.site.register(Careers)
admin.site.register(Curriculums)
admin.site.register(CoursePrerequisites)
admin.site.register(Courses)
admin.site.register(Professors)
admin.site.register(Groups)
admin.site.register(CourseLoads)
admin.site.register(Semesters)
admin.site.register(AcademicDegrees)
admin.site.register(AcademicSemesters)
admin.site.register(Users)
admin.site.register(Students)
admin.site.register(Professions)
