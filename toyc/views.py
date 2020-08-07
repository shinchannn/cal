from django.views.generic import ListView, CreateView
from .models import Record
from django.urls import reverse

class RecordsView(CreateView):
    model = Record
    template_name = 'index.html'
    fields = ['content']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["records"] = self.model.objects.all().order_by('-posted_on')[0:10]
        return context

    def get_success_url(self):
        return reverse('index')