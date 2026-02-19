from django.views.generic import TemplateView
from django.db.models import Sum
from .models import Department

class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Annotate total asset cost per department
        context['department_costs'] = Department.objects.annotate(total_cost=Sum('users__assets__cost'))
        return context
