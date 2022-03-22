from django import forms

class LeaveForm(forms.Form):
    leave_choice = (
        ('S', 'Sick_leave'),
        ('P', 'Personal')
    )
    
    traineeid = forms.IntegerField()
    name = forms.CharField()
    leaveType = forms.ChoiceField(choices=leave_choice)
    date = forms.DateField()
    NoLeaves = forms.IntegerField()
    leave_message = forms.CharField(max_length=10000)


class ClientForm(forms.Form):

    company_name = forms.CharField( max_length=255)
    # image = forms.ImageField()
    CompanyLink = forms.CharField(max_length = 255)
    email = forms.CharField(max_length = 255)
    Contact1 = forms.IntegerField()
    Contact2 =forms.IntegerField()
    Address = forms.CharField( max_length=1000)
    OrganisationType = forms.CharField(max_length = 150)
    NOB = forms.CharField(max_length = 150)
    RegisterdOffice = forms.IntegerField()
    Name = forms.CharField(max_length = 150)
    emailid = forms.EmailField(max_length=255)
    TelephoneNO = forms.IntegerField()
    Position = forms.CharField(max_length=150)

class PayrollForm(forms.Form):
    staff_id = forms.IntegerField()
    rate_per_day = forms.IntegerField()
    days_present = forms.IntegerField()
    leaves_with_pay = forms.IntegerField()
    base_income = forms.IntegerField()
    ot_rate = forms.IntegerField() #over time bonous
    ot_hours = forms.IntegerField()
    total_amount_ot = forms.IntegerField()
    other_reason = forms.CharField(max_length=255)
    other_amount = forms.IntegerField()
    totat_other_amount = forms.IntegerField()
    net_salary = forms.IntegerField()
    salary_status = forms.BooleanField(required=False)