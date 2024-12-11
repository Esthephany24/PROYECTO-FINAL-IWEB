# Generated by Django 5.1.4 on 2024-12-11 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicDegrees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.IntegerField()),
                ('created', models.DateTimeField()),
                ('modified', models.DateTimeField(blank=True, null=True)),
                ('created_id', models.IntegerField()),
                ('modified_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'academic_degrees',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AcademicSemesters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('status', models.IntegerField()),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('modified', models.DateTimeField(blank=True, null=True)),
                ('created_id', models.IntegerField()),
                ('modified_id', models.IntegerField(blank=True, null=True)),
                ('academic_year', models.IntegerField()),
                ('period', models.CharField(max_length=100)),
                ('semester_type', models.CharField(max_length=100)),
                ('weeks_count', models.IntegerField()),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'academic_semesters',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Areas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('status', models.IntegerField()),
                ('created', models.DateTimeField()),
                ('modified_date', models.DateTimeField(blank=True, null=True)),
                ('created_id', models.IntegerField()),
                ('modified_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'areas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Careers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.IntegerField()),
                ('created', models.DateTimeField()),
                ('modified', models.DateTimeField(blank=True, null=True)),
                ('created_id', models.IntegerField()),
                ('modified_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'careers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CourseLoads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.IntegerField()),
                ('created', models.DateTimeField()),
                ('modified', models.DateTimeField(blank=True, null=True)),
                ('created_id', models.IntegerField()),
                ('modified_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'course_loads',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CoursePrerequisites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField()),
                ('created', models.DateTimeField()),
                ('modified', models.DateTimeField(blank=True, null=True)),
                ('created_id', models.IntegerField()),
                ('modified_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'course_prerequisites',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('code', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('theory_hours', models.IntegerField()),
                ('practice_hours', models.IntegerField()),
                ('lab_hours', models.IntegerField()),
                ('total_hours', models.IntegerField(blank=True, null=True)),
                ('summary', models.TextField(blank=True, null=True)),
                ('credits', models.IntegerField()),
                ('semi_hours', models.IntegerField(blank=True, null=True)),
                ('status', models.IntegerField()),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('modified', models.DateTimeField(blank=True, null=True)),
                ('created_id', models.IntegerField()),
                ('modified_id', models.IntegerField(blank=True, null=True)),
                ('theory_pracs_hours', models.IntegerField(blank=True, null=True)),
                ('prq_cred', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'courses',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Curriculums',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField()),
                ('tag', models.CharField(blank=True, max_length=255, null=True)),
                ('created', models.DateTimeField()),
                ('modified', models.DateTimeField(blank=True, null=True)),
                ('created_id', models.IntegerField()),
                ('modified_id', models.IntegerField(blank=True, null=True)),
                ('culmination', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'curriculums',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.IntegerField()),
                ('created', models.DateTimeField()),
                ('modified', models.DateTimeField(blank=True, null=True)),
                ('created_id', models.IntegerField()),
                ('modified_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'departments',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Faculties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.IntegerField()),
                ('created', models.DateTimeField()),
                ('modified', models.DateTimeField(blank=True, null=True)),
                ('created_id', models.IntegerField()),
                ('modified_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'faculties',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('code', models.IntegerField()),
                ('status', models.IntegerField()),
                ('created', models.DateTimeField()),
                ('modified', models.DateTimeField(blank=True, null=True)),
                ('created_id', models.IntegerField()),
                ('modified_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Professions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.IntegerField()),
                ('created', models.DateTimeField()),
                ('modified', models.DateTimeField(blank=True, null=True)),
                ('created_id', models.IntegerField()),
                ('modified_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'professions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Professors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('father_surname', models.CharField(max_length=50)),
                ('mother_surname', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=1)),
                ('profession_id', models.IntegerField()),
                ('birthdate', models.DateField()),
                ('nationality', models.CharField(max_length=50)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('status', models.IntegerField()),
                ('created', models.DateTimeField()),
                ('modified', models.DateTimeField(blank=True, null=True)),
                ('created_id', models.IntegerField()),
                ('modified_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'professors',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Semesters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('details', models.CharField(max_length=200)),
                ('status', models.IntegerField()),
                ('created', models.DateTimeField()),
                ('modified', models.DateTimeField(blank=True, null=True)),
                ('created_id', models.IntegerField()),
                ('modified_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'semesters',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('father_surname', models.CharField(max_length=50)),
                ('mother_surname', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=1)),
                ('birthdate', models.DateField()),
                ('nationality', models.CharField(max_length=50)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('status', models.IntegerField()),
                ('created', models.DateTimeField()),
                ('modified', models.DateTimeField(blank=True, null=True)),
                ('create_id', models.IntegerField()),
                ('modified_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'students',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Universities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('url', models.TextField(blank=True, null=True)),
                ('acronym', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.IntegerField()),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('modified', models.DateTimeField(blank=True, null=True)),
                ('created_id', models.IntegerField()),
                ('modified_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'universities',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('father_surname', models.CharField(max_length=50)),
                ('mother_surname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=400)),
                ('status', models.IntegerField()),
                ('created', models.DateTimeField()),
                ('modified', models.DateTimeField(blank=True, null=True)),
                ('created_id', models.IntegerField()),
                ('modified_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
    ]