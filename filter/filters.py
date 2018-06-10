import django_filters
from django import forms
from .models import Phone

class PhoneFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(name='name', lookup_expr='icontains')
    brand = django_filters.CharFilter(name='brand', lookup_expr='icontains')
    data_transfer = django_filters.CharFilter(name='data_transfer', lookup_expr='icontains')
    operating_system = django_filters.CharFilter(name='operating_system', lookup_expr='icontains')
    processor_speed = django_filters.filters.ModelMultipleChoiceFilter(
                                                queryset=Phone.objects.all(),
                                                to_field_name='processor_speed',
                                                widget=forms.CheckboxSelectMultiple)
    price__gt = django_filters.NumberFilter(name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(name='price', lookup_expr='lt')

    class Meta:
        model = Phone
        fields = ['name']
