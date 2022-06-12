from rest_framework import generics


# class CompanyListView(generics.ListCreateAPIView):
#     serializer_class = service.ServiceSerializer
#     permission_classes = [user_permissions.IsCompanyUser]
#
#     def get_queryset(self):
#         return models.Service.objects.select_related("company").filter(
#             company=self.request.user.company
#         )