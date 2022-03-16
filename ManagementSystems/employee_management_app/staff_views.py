from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


def Attendance_show(request):
    return render(request, 'app/attendance.html')


def mark_attendance(request):
    current_user = request.user
    print(current_user)
    date_time = datetime.now()
    date = datetime.now().today().date()
    time = datetime.now().strftime("%H:%M:%S")
    print(date_time, time , date)
    current_user.last_login = date_time = datetime.now()
    print(current_user.last_login)
    current_user.save()
    return HttpResponse("attendance marked!")
