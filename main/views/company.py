from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from main.serailizers import company

from users import permissions as user_permissions
from rest_framework.permissions import IsAuthenticated
from main import models, filters


class CompanyListView(generics.ListAPIView):
    serializer_class = company.CompanySerializer
    permission_classes = [IsAuthenticated]
    # permission_classes = [user_permissions.IsStaffUser]
    queryset = models.Company.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.CompanyFilter
