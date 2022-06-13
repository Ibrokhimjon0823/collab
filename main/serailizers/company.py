from rest_framework import serializers

from main import models


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Company
        fields = "__all__"

