from rest_framework import generics

from users import permissions as user_permissions
from rest_framework.permissions import IsAuthenticated
from . import models, serializers


class ServiceListCreateView(generics.ListCreateAPIView):
    serializer_class = serializers.ServiceSerializer
    permission_classes = [user_permissions.IsCompanyUser]

    def get_queryset(self):
        return models.Service.objects.select_related("company").filter(
            company=self.request.user.company
        )


class ServiceListView(generics.ListAPIView):
    serializer_class = serializers.ServiceSerializer
    permission_classes = [IsAuthenticated, ]


class ServiceRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.ServiceSerializer
    permission_classes = [user_permissions.IsCompanyUser]

    def get_queryset(self):
        return models.Service.objects.select_related("company").filter(
            company=self.request.user.company
        )
