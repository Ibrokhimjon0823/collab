from django.urls import path

from . import views

urlpatterns = [
    path("service/", views.ServiceListCreateView.as_view(), name="service-list-create"),
    path(
        "service/<int:pk>/",
        views.ServiceRetrieveUpdateDeleteView.as_view(),
        name="service-retrieve-update-delete",
    ),
]
