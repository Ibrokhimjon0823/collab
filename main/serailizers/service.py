from rest_framework import serializers

from core.utils import send_registration_email, request_create_email_message
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
        data._mutable = True
        data['customer'] = request.user.id
        return super().to_internal_value(data)

    class Meta:
        model = Request
        fields = [
            'id',
            'customer',
            'service',
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
        request = Request.objects.create(**validated_data)
        Notification.objects.create(company=request.service.company, request=request)
        send_registration_email(request.service.company.owner.email, request_create_email_message())
        return request


class StatusChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ['status']
        extra_kwargs = {
            'status': {'required': True}
        }