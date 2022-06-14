from rest_framework import serializers

from main import models
from main.models import Request, Notification


class CurrentCompanyDefault:
    requires_context = True

    def __call__(self, serializer_field):
        return serializer_field.context["request"].user.company

    def __repr__(self):
        return "%s()" % self.__class__.__name__


class ServiceSerializer(serializers.ModelSerializer):
    company = serializers.HiddenField(default=CurrentCompanyDefault())

    class Meta:
        model = models.Service
        fields = ("id", "name", "price", "company")


class RequestSerializer(serializers.ModelSerializer):

    def to_internal_value(self, data):
        request = self.context.get('request')
        data['customer'] = request.user.id
        return super().to_internal_value(data)

    class Meta:
        model = Request
        fields = [
            'id',
            'customer',
            'companies',
            'country',
            'city',
            'street',
            'house_number',
            'apartment',
            'status',
            'duration',
            'area',
        ]

    def create(self, validated_data):
        companies = validated_data.pop('companies')
        request = Request.objects.create(**validated_data)
        request.companies.add(*companies)
        for company in request.companies.all():
            Notification.objects.create(company=company, request=request)
        return request
