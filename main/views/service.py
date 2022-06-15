from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.viewsets import ModelViewSet

from main.models import Request
from users import permissions as user_permissions
from rest_framework.permissions import IsAuthenticated
from main import models, filters
from main.serailizers import company, service, RequestSerializer
from users.admin import CustomUser


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
    queryset = models.Service.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.ServiceFilter


class ServiceRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = service.ServiceSerializer
    permission_classes = [user_permissions.IsCompanyUser]

    def get_queryset(self):
        return models.Service.objects.select_related("company").filter(
            company=self.request.user.company
        )


class RequestViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

    # def get_queryset(self):
    #     if self.request.user.role == "customer":
    #         return self.get_queryset().filter(customer=self.request.user)
    #     else:
    #         return self.get_queryset().filter(companies__in=[self.request.user.company])


