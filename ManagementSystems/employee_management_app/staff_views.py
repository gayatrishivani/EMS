from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.shortcuts import render

from .models import Attendance, Staff


def Attendance_show(request):
    current_user = request.user
    id = current_user.id
    name = current_user.first_name

    staff = Staff.objects.get(admin__id = current_user.id)
    attendance = Attendance.objects.filter(staff_id = staff)
    print(attendance)

    context = {
        'id' : id,
        'name' : name,
        'attendance': attendance
    }
    return render(request, 'app/attendance.html', context=context)


def mark_attendance(request):
    print('ajax is passed')
    print(request)
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
    return HttpResponse("This is working")