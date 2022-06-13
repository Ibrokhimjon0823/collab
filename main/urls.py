from django.urls import path
from rest_framework.routers import SimpleRouter

from main import views
from .views import RequestViewSet
from .views.rating import RatingViewSet

router = SimpleRouter()
router.register(r'rating', RatingViewSet, basename="rating")
router.register(r'request', RequestViewSet, basename="request")
urlpatterns = router.urls

urlpatterns += [
    path("service/", views.ServiceListCreateView.as_view(), name="service-list-create"),
    path(
        "service/<int:pk>/",
        views.ServiceRetrieveUpdateDeleteView.as_view(),
        name="service-retrieve-update-delete",
    ),
    path('company/', views.CompanyListView.as_view(), name="company-list"),
]
