from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.shortcuts import redirect, render

from .forms import LeaveForm

from .models import Attendance, Leave, Staff


def Attendance_show(request):
    current_user = request.user
    id = current_user.id
    name = current_user.first_name

    staff = Staff.objects.get(admin__id = current_user.id)
    attendance = Attendance.objects.filter(staff_id = staff)
    context = {
        'id' : id,
        'name' : name,
        'attendance': attendance
    }
    return render(request, 'app/attendance.html', context=context)


def mark_attendance(request):
    print('ajax is passed')
    if request.method == 'POST' :
        current_user = request.user
        staff = Staff.objects.get(admin__id=current_user.id)
        attendance = Attendance()
        attendance.is_present = True
        attendance.staff_id = staff
        attendance.save()
        inst = attendance
        arrival = 'you are late'
        json_instance = serializers.serialize('json', [inst, ])
        return JsonResponse({"instance": json_instance, "arrival": arrival}, status=200)
    else:
        return HttpResponse("cannot do that!")

def request_leave(request):
    if request.method == 'POST':
        form = LeaveForm(request.POST)
        if form.is_valid():
            traineeid = form.cleaned_data["traineeid"]
            name = form.cleaned_data["name"]
            leaveType = form.cleaned_data["leaveType"]
            date =  form.cleaned_data["date"]
            NoLeaves = form.cleaned_data["NoLeaves"]
            leave_message = form.cleaned_data["leave_message"]

            try:
                leave = Leave()
                staff = Staff.objects.get(admin__id=traineeid)
                leave.staff_id = staff
                leave.leave_type = leaveType
                leave.no_of_leaves = NoLeaves
                leave.leave_message = leave_message
                leave.save()
                messages.success(request, "leave is submitted")
                return redirect('/attendance')
            except:
                messages.error(request,"failed")
                return HttpResponse("faied to add leave")
        else:
            return HttpResponse("This is working")
        
    