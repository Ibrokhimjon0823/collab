import django_filters

from main.models import Company, Service


class CompanyFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Company
        fields = ['owner', 'name']


class ServiceFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Service
        fields = ['company', 'name', 'price']
