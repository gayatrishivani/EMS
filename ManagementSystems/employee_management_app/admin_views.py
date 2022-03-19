from django.http import HttpResponse
from django.shortcuts import render


def client_view(request):
    return render(request, 'admin/client.html')