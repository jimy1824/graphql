from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView, CreateView
import datetime


class DashboardView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        # kwargs['appointments'] = Schedule.objects.filter(
        #     tenant=self.request.user.tenant,
        #     is_completed=False,
        #     date__gte=today
        # ).order_by('date')
        return kwargs
