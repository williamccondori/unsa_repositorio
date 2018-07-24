from django.shortcuts import render
from django.http import HttpResponse

def dashboard(request):
    return render(request, 'admin/dashboard.html')

def manage(request):
    return render(request, 'admin/manage.html')