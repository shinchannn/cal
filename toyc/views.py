from .models import Record
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def dashboard(request):
    if request.method == "POST":
        record = Record()
        record.content = request.POST.get("temp")
        record.save()
        return render(request, "index.html")
    else:
        return render(request, "index.html")

def records(request):
    latest_records_list = list(Record.objects.values().order_by('-posted_on')[0:10])
    #latest_records_list = list(Record.objects.all().order_by('-posted_on')[0:10])
    #template = loader.get_template("index.html")
    #context = {'latest_records_list': latest_records_list}

    return JsonResponse(latest_records_list, safe=False)