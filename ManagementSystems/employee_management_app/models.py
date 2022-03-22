from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    user_type_data = ((1, "AdminMan"), (2, "Staff"))
    user_type = models.CharField(default=1,choices=user_type_data, max_length=10 )


#AdminMan calss
class AdminMan(models.Model):
    id = models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.FileField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()


class Staff(models.Model):
    Gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others')
    )
    id =models.AutoField(primary_key=True)
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.FileField(blank=True, null=True)
    gender = models.CharField(max_length = 10, default='O', choices=Gender_choices)
    is_trainee = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    address = models.TextField(blank=True, null=True)
    objects = models.Manager()


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    company_link = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    contact1 = models.IntegerField()
    contact2 =models.IntegerField()
    address = models.TextField()
    affliated_company = models.CharField(max_length = 255)
    organisation_type = models.CharField(max_length = 150)
    nature_of_bussines = models.CharField(max_length = 150)
    registered_office = models.IntegerField()
    owner_name = models.CharField(max_length = 150)
    email = models.EmailField(max_length=255)
    telephone = models.IntegerField()
    owner_positon = models.CharField(max_length=150)
    # assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    objects = models.Manager()


class Assignment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 255)
    satff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    clients_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    AdminMan_id = models.ForeignKey(AdminMan, on_delete=models.CASCADE)
    is_compleated = models.BooleanField()
    created_at = models.DateTimeField(  auto_now_add=True)
    updated_at = models.DateTimeField(  auto_now_add= True)
    objects = models.Manager()


class Attendance(models.Model):
    id = models.AutoField(primary_key=True)
    is_present = models.BooleanField()
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    log_time = models.DateTimeField(  auto_now_add=True)
    objects = models.Manager()

class Leave(models.Model):
    leave_choice = (
        ('S', 'Sick_leave'),
        ('P', 'Personal')
    )
    id = models.AutoField(primary_key=True)
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=1, choices=leave_choice)
    no_of_leaves = models.IntegerField()
    leave_message = models.TextField()
    created_at = models.DateTimeField(  auto_now_add=True)
    objects = models.Manager()


class Payroll(models.Model):
    id = models.AutoField(primary_key=True)
    AdminMan_id = models.ForeignKey(AdminMan, on_delete=models.CASCADE)
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    rate_per_day = models.IntegerField()
    days_present = models.IntegerField()
    month_pay = models.CharField(max_length=100)
    leaves_with_pay = models.IntegerField()
    base_income = models.IntegerField()
    ot_rate = models.IntegerField() #over time bonous
    ot_hours = models.IntegerField()
    total_amount_ot = models.IntegerField()
    other_reason = models.CharField(max_length=255)
    other_amount = models.IntegerField()
    totat_other_amount = models.IntegerField()
    net_salary = models.IntegerField()
    salary_status = models.BooleanField()
    objects = models.Manager()


class Notice(models.Model):
    id = models.AutoField(primary_key=True)
    AdminMan_id = models.ForeignKey(AdminMan, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(  auto_now_add=True)
    objects = models.Manager()


@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            AdminMan.objects.create(admin=instance)
        if instance.user_type==2:
            Staff.objects.create(admin=instance)    
@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.adminman.save()
    if instance.user_type==2:
        instance.staff.save()
