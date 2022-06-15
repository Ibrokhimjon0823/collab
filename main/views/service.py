from rest_framework import generics, status
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from core.utils import send_registration_email
from main.models import Request
from users import permissions as user_permissions
from rest_framework.permissions import IsAuthenticated
from main import models, filters
from main.serailizers import company, service, RequestSerializer, StatusChangeSerializer
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

    @action(methods=['POST'], detail=True, url_name='status-change', url_path='status-change')
    def status_change(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = StatusChangeSerializer(
            instance=instance,
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        request_status = serializer.validated_data.get('status')
        serializer.save()
        if request_status == Request.Status.APPROVED:
            message = f"Your request has been {request.data.get('status')}. The total cost of service is {instance.total_cost} "
        else:
            message = f"Your request has been {request.data.get('status')}"
        send_registration_email(instance.customer.email, message)
        return Response({"message":"Request Status has been changed!"},status=status.HTTP_200_OK)

