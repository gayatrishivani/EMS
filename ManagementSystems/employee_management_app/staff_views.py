from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.shortcuts import render

from .models import Attendance, Staff


def Attendance_show(request):
    return render(request, 'app/attendance.html')


def mark_attendance(request):
    if request.is_ajax:
        current_user = request.user
        staff = Staff.objects.get(admin__id=current_user.id)
        attendance = Attendance()
        attendance.is_present = True
        attendance.staff_id = staff
        inst = attendance.save()
        arrival = 'you are late'
        json_instance = serializers.serialize('json', [inst, ])
        return JsonResponse({"instance": json_instance, 'arrival':arrival}, status=200)
    else:
        return HttpResponse("cannot do that!")
