from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from .models import DailyReport

@staff_member_required
def report_list(request):
    reports = DailyReport.objects.order_by('-date')
    return render(request, 'analytics/report_list.html', {'reports': reports})
