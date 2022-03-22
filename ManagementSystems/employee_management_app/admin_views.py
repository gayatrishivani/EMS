from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import AdminMan, Attendance, Client, Leave, Payroll, Staff

from .forms import ClientForm, PayrollForm
from datetime import datetime

def client_view(request):
    return render(request, 'admin/client.html')

def add_client(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            company_name = form.cleaned_data["company_name"]
            # image = form.ImageField()
            CompanyLink = form.cleaned_data["CompanyLink"]
            email = form.cleaned_data["email"]
            Contact1 = form.cleaned_data["Contact1"]
            Contact2 =form.cleaned_data["Contact2"]
            Address = form.cleaned_data["Address"]
            OrganisationType = form.cleaned_data["OrganisationType"]
            NOB = form.cleaned_data["NOB"]
            RegisterdOffice = form.cleaned_data["RegisterdOffice"]
            Name = form.cleaned_data["Name"]
            emailid = form.cleaned_data["emailid"]
            TelephoneNO = form.cleaned_data["TelephoneNO"]
            Position = form.cleaned_data["Position"]

            try:
                client = Client()
                client.company_name = company_name
                client.email =email
                client.contact1 = Contact1
                client.contact2 = Contact2
                client.address = Address
                client.organisation_type = OrganisationType
                client.nature_of_bussines = NOB
                client.registered_office = RegisterdOffice
                client.owner_name = Name
                client.telephone = TelephoneNO
                client.owner_positon = Position
                client.save()
                messages.success(request, "client added")
            except:
                messages.error(request, "failed to added client")
            return HttpResponseRedirect("/client")
        else:
            return HttpResponse("form not valid")
    else:
        return HttpResponse("this is not valid response")

def admin_attendance(request):
    attendance_list = Attendance.objects.all()
    page_aten = request.GET.get('page-aten', 1)
    leaves_list = Leave.objects.all()
    page_leave = request.GET.get("page-leave", 1)
    
    paginator_aten = Paginator(attendance_list, 10)
    paginator_leave = Paginator(leaves_list, 10)

    try:
        attendance = paginator_aten.page(page_aten)
        leaves = paginator_leave.page(page_leave)
    
    except PageNotAnInteger:
        attendance = paginator_aten.page(1)
        leaves = paginator_leave.page(1)
    
    except EmptyPage:
        attendance = paginator_aten.page(paginator_aten.num_pages)
        leaves = paginator_leave.page(paginator_leave.num_pages)
    context = {
        'attendance':attendance,
        'leaves': leaves
    }
    return render(request, 'admin/attendance.html', context=context)

def payroll_view(request):
    payroll_list = Payroll.objects.all()
    page_roll = request.GET.get('page-roll',1)
    paginator_roll = Paginator(payroll_list, 10)
    
    try:
        pays = paginator_roll.page(page_roll)
    
    except PageNotAnInteger:
        pays = paginator_roll.page(1)
        
    
    except EmptyPage:
        pays = paginator_roll.page(paginator_roll.num_pages)
        
    
    context ={
        'pays': pays
    }

    return render(request, 'admin/payroll.html', context=context)

def add_payroll(request):

    return render(request, 'admin/add_payroll.html')

def adding_payroll(request):

    if request.method == "POST":
        user = request.user
        print(user)
        form  = PayrollForm(request.POST)
        print(form)
        if form.is_valid():
            
            staff_id = form.cleaned_data["staff_id"]
            rate_per_day = form.cleaned_data["rate_per_day"]
            days_present = form.cleaned_data["days_present"]
            leaves_with_pay = form.cleaned_data["leaves_with_pay"]
            base_income = form.cleaned_data["base_income"]
            ot_rate = form.cleaned_data["ot_rate"] #over time bonous
            ot_hours = form.cleaned_data["ot_hours"]
            total_amount_ot = form.cleaned_data["total_amount_ot"]
            other_reason = form.cleaned_data["other_reason"]
            other_amount = form.cleaned_data["other_amount"]
            totat_other_amount = form.cleaned_data["totat_other_amount"]
            net_salary = form.cleaned_data["net_salary"]
            salary_status = form.cleaned_data["salary_status"]

            try:
                payroll = Payroll()
                print(payroll)
                payroll.AdminMan_id = AdminMan.objects.get(admin__id = user.id)
                staff = Staff.objects.get(admin__id = staff_id)
                payroll.staff_id = staff
                payroll.rate_per_day = rate_per_day
                payroll.days_present = days_present
                payroll.leaves_with_pay = leaves_with_pay
                payroll.base_income = base_income
                payroll.ot_rate = ot_rate
                payroll.ot_hours = ot_hours
                payroll.total_amount_ot = total_amount_ot
                payroll.other_reason = other_reason
                payroll.other_amount = other_amount
                payroll.totat_other_amount = totat_other_amount
                payroll.net_salary = net_salary
                
                payroll.salary_status = salary_status
                payroll.month_pay = datetime.now().month
                
                payroll.save()

            except:
                messages.error(request, "failed to added client")
            
            return HttpResponseRedirect("/adding-payroll")

        else:
            return HttpResponse("form is invalid")
        

    else:
        return HttpResponseRedirect("/adding-payroll")