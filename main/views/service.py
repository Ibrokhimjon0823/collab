from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from main.models import Request
from users import permissions as user_permissions
from rest_framework.permissions import IsAuthenticated
from main import models
from main.serailizers import company, service, RequestSerializer


class ServiceListCreateView(generics.ListCreateAPIView):
    serializer_class = service.ServiceSerializer
    permission_classes = [user_permissions.IsCompanyUser]

    def get_queryset(self):
        return models.Service.objects.select_related("company").filter(
            company=self.request.user.company
        )


class ServiceListView(generics.ListAPIView):
    serializer_class = service.ServiceSerializer
    permission_classes = [IsAuthenticated, ]


class ServiceRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = service.ServiceSerializer
    permission_classes = [user_permissions.IsCompanyUser]

    def get_queryset(self):
        return models.Service.objects.select_related("company").filter(
            company=self.request.user.company
        )


class RequestViewSet(ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer




