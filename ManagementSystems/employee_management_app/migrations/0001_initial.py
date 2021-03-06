# Generated by Django 4.0.3 on 2022-03-16 03:16

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(choices=[(1, 'AdminMan'), (2, 'Staff')], default=1, max_length=10)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AdminMan',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to=None)),
                ('company_link', models.CharField(max_length=255)),
                ('contact1', models.IntegerField()),
                ('contact2', models.IntegerField()),
                ('address', models.TextField()),
                ('affliated_company', models.CharField(max_length=255)),
                ('organisation_type', models.CharField(max_length=150)),
                ('nature_of_bussines', models.CharField(max_length=150)),
                ('registered_office', models.IntegerField()),
                ('owner_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=255)),
                ('telephone', models.IntegerField()),
                ('owner_positon', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], default='O', max_length=10)),
                ('is_trainee', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payroll',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rate_per_day', models.BigIntegerField()),
                ('days_present', models.IntegerField()),
                ('leaves_with_pay', models.IntegerField()),
                ('base_income', models.IntegerField()),
                ('ot_rate', models.BigIntegerField()),
                ('ot_hours', models.IntegerField()),
                ('total_amount_ot', models.BigIntegerField()),
                ('other_reason', models.CharField(max_length=255)),
                ('other_amount', models.BigIntegerField()),
                ('totat_other_amount', models.IntegerField()),
                ('net_salary', models.BigIntegerField()),
                ('salary_status', models.BooleanField()),
                ('AdminMan_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_management_app.adminman')),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_management_app.staff')),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('AdminMan_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_management_app.adminman')),
            ],
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('leave_type', models.CharField(choices=[('S', 'Sick_leave'), ('P', 'Personal')], max_length=1)),
                ('no_of_leaves', models.IntegerField()),
                ('leave_message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_management_app.staff')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_present', models.BooleanField()),
                ('log_time', models.DateTimeField(auto_now_add=True)),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_management_app.staff')),
            ],
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('is_compleated', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('AdminMan_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_management_app.adminman')),
                ('clients_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_management_app.client')),
                ('satff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_management_app.staff')),
            ],
        ),
    ]
