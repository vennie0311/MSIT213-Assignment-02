from django.views.generic import TemplateView, ListView, CreateView
from django.db.models import Sum
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .models import Department, Asset, MaintenanceLog


class DashboardView(TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['department_costs'] = Department.objects.annotate(
            total_cost=Sum('users__assets__cost')
        )
        return context


class AssetListView(ListView):
    model = Asset
    template_name = 'asset_list.html'
    context_object_name = 'assets'

    def get_queryset(self):
        return Asset.objects.annotate(
            repair_total=Sum('maintenance_logs__cost')
        )


class MaintenanceCreateView(CreateView):
    model = MaintenanceLog
    fields = ['description', 'cost', 'date_repaired']
    template_name = 'maintenance_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.asset = get_object_or_404(Asset, pk=self.kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.asset = self.asset
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('asset_list')