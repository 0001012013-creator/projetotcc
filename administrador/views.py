from django.shortcuts import render

def dashboard_adm(request):
    return render(request, 'accounts/dashboardadm.html')