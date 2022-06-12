from rest_framework import serializers

from . import models


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
