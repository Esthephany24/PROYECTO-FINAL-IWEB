# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AcademicDegrees(models.Model):
    name = models.CharField(max_length=100)
    status = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)
    created_id = models.IntegerField()
    modified_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'academic_degrees'

    def _str_(self):
        return self.name


class AcademicSemesters(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    created_id = models.IntegerField()
    modified_id = models.IntegerField(blank=True, null=True)
    academic_year = models.IntegerField()
    period = models.CharField(max_length=100)
    semester_type = models.CharField(max_length=100)
    weeks_count = models.IntegerField()
    description = models.TextField(blank=True, null=True)

    

    class Meta:
        managed = False
        db_table = 'academic_semesters'

    def _str_(self):                                                   return self.name


class Areas(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    status = models.IntegerField()
    created = models.DateTimeField()
    modified_date = models.DateTimeField(blank=True, null=True)
    created_id = models.IntegerField()
    modified_id = models.IntegerField(blank=True, null=True)

    def _str_(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'areas'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'
    
    
class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)
    

class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)
    

class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'
    

class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)
    
class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Careers(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)
    created_id = models.IntegerField()
    modified_id = models.IntegerField(blank=True, null=True)
    department = models.ForeignKey('Departments', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'careers'

    def _str_(self):                                                   return self.name


class CourseLoads(models.Model):
    details = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)
    created_id = models.IntegerField()
    modified_id = models.IntegerField(blank=True, null=True)
    professor = models.ForeignKey('Professors', models.DO_NOTHING)
    course = models.ForeignKey('Courses', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'course_loads'

    def _str_(self):                                                   return self.details


class CoursePrerequisites(models.Model):
    course = models.ForeignKey('Courses', models.DO_NOTHING)
    prerequisite = models.ForeignKey('Courses', models.DO_NOTHING, related_name='courseprerequisites_prerequisite_set')
    status = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)
    created_id = models.IntegerField()
    modified_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course_prerequisites'

    def _str_(self):                                                   return self.course


class Courses(models.Model):
    area = models.ForeignKey(Areas, models.DO_NOTHING)
    name = models.CharField(max_length=300)
    code = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    theory_hours = models.IntegerField()
    practice_hours = models.IntegerField()
    lab_hours = models.IntegerField()
    total_hours = models.IntegerField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    credits = models.IntegerField()
    semi_hours = models.IntegerField(blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    created_id = models.IntegerField()
    modified_id = models.IntegerField(blank=True, null=True)
    semester = models.ForeignKey('Semesters', models.DO_NOTHING)
    theory_pracs_hours = models.IntegerField(blank=True, null=True)
    prq_cred = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'courses'

    def _str_(self):                                                   return self.name


class Curriculums(models.Model):
    status = models.IntegerField()
    tag = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)
    created_id = models.IntegerField()
    modified_id = models.IntegerField(blank=True, null=True)
    culmination = models.DateField(blank=True, null=True)
    careers = models.ForeignKey(Careers, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'curriculums'

    def _str_(self):                                                   return self.tag


class Departments(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)
    created_id = models.IntegerField()
    modified_id = models.IntegerField(blank=True, null=True)
    faculty = models.ForeignKey('Faculties', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'departments'

    def _str_(self):                                                   return self.name


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'

    
class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)



class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'

    def _str_(self):                                                   return self.name


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Faculties(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)
    created_id = models.IntegerField()
    modified_id = models.IntegerField(blank=True, null=True)
    university = models.ForeignKey('Universities', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'faculties'

    def _str_(self):                                                   return self.name


class Groups(models.Model):
    name = models.CharField(max_length=30)
    code = models.IntegerField()
    status = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)
    created_id = models.IntegerField()
    modified_id = models.IntegerField(blank=True, null=True)
    course = models.ForeignKey(Courses, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'groups'

    def _str_(self):                                                   return self.name


class Professions(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)
    created_id = models.IntegerField()
    modified_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'professions'

    def _str_(self):                                                   return self.name


class Professors(models.Model):
    first_name = models.CharField(max_length=100)
    father_surname = models.CharField(max_length=50)
    mother_surname = models.CharField(max_length=50)
    gender = models.CharField(max_length=1)
    profession_id = models.IntegerField()
    birthdate = models.DateField()
    nationality = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)
    created_id = models.IntegerField()
    modified_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'professors'

    def _str_(self):                                                   return self.first_name


class Semesters(models.Model):
    name = models.CharField(max_length=50)
    details = models.CharField(max_length=200)
    status = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)
    created_id = models.IntegerField()
    modified_id = models.IntegerField(blank=True, null=True)
    curriculum = models.ForeignKey(Curriculums, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'semesters'

    def _str_(self):                                                   return self.name


class Students(models.Model):
    first_name = models.CharField(max_length=50)
    father_surname = models.CharField(max_length=50)
    mother_surname = models.CharField(max_length=50)
    gender = models.CharField(max_length=1)
    birthdate = models.DateField()
    nationality = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(unique=True, max_length=100)
    status = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)
    create_id = models.IntegerField()
    modified_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students'
    def _str_(self):                                                   return self.first_name


class Universities(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    acronym = models.CharField(max_length=50, blank=True, null=True)
    status = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    created_id = models.IntegerField()
    modified_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'universities'

    def _str_(self):                                                   return self.name


class Users(models.Model):
    first_name = models.CharField(max_length=100)
    father_surname = models.CharField(max_length=50)
    mother_surname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=400)
    status = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField(blank=True, null=True)
    created_id = models.IntegerField()
    modified_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'

    def _str_(self):                                                   return self.first_name
