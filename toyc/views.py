from .models import Record
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def dashboard(request):
    return render(request, "index.html")

def save(request):
    # POST data
    record = Record()
    record.content = request.POST.get("temp")
    record.save()
    return HttpResponse(None)

def records(request):
    latest_records_list = list(Record.objects.values().order_by('-posted_on')[0:10])
    return JsonResponse(latest_records_list, safe=False)