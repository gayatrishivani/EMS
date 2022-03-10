# Generated by Django 4.0.3 on 2022-03-10 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to=None)),
                ('email', models.EmailField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Admin',
                'verbose_name_plural': 'Admins',
                'db_table': '',
                'managed': True,
            },
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
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to=None)),
                ('email', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], max_length=1)),
                ('is_staff', models.BooleanField()),
                ('password', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('address', models.TextField()),
            ],
            options={
                'verbose_name': 'Staff',
                'verbose_name_plural': 'Staffs',
                'db_table': '',
                'managed': True,
            },
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
                ('admin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_management_app.admin')),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_management_app.staff')),
            ],
            options={
                'verbose_name': 'Payroll',
                'verbose_name_plural': 'Payrolls',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('admin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_management_app.admin')),
            ],
            options={
                'verbose_name': 'Notice',
                'verbose_name_plural': 'Notices',
                'db_table': '',
                'managed': True,
            },
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
            options={
                'verbose_name': 'Leave',
                'verbose_name_plural': 'Leaves',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_present', models.BooleanField()),
                ('log_time', models.DateTimeField(auto_now_add=True)),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_management_app.staff')),
            ],
            options={
                'verbose_name': 'Attendance',
                'verbose_name_plural': 'Attendances',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('is_compleated', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('admin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_management_app.admin')),
                ('clients_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_management_app.client')),
                ('satff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_management_app.staff')),
            ],
            options={
                'verbose_name': 'Assignment',
                'verbose_name_plural': 'Assignments',
                'db_table': '',
                'managed': True,
            },
        ),
    ]