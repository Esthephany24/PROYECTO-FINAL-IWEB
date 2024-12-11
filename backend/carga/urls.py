from django.urls import path, include
from rest_framework.routers import DefaultRouter
from carga.views import *

router = DefaultRouter()
router.register(r'universities', UniversitiesViewSet)
router.register(r'faculties', FacultiesViewSet)
router.register(r'departments', DepartmentsViewSet)
router.register(r'areas', AreasViewSet)
router.register(r'careers', CareersViewSet)
router.register(r'curriculums', CurriculumsViewSet)
router.register(r'course_prerequisites', CoursePrerequisitesViewSet)
router.register(r'courses', CoursesViewSet)
router.register(r'professors', ProfessorsViewSet)
router.register(r'groups', GroupsViewSet)
router.register(r'course_loads', CourseLoadsViewSet)
router.register(r'semesters', SemestersViewSet)
router.register(r'academic_degrees', AcademicDegreesViewSet)
router.register(r'academic_semesters', AcademicSemestersViewSet)
router.register(r'users', UsersViewSet)
router.register(r'students', StudentsViewSet)
router.register(r'professions', ProfessionsViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
]

