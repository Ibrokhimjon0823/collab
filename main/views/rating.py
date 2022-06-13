from rest_framework.viewsets import ModelViewSet

from main.models import Rating
from main.serailizers.rating import RatingCreateSerializer, RatingGetSerializer


class RatingViewSet(ModelViewSet):
    queryset = Rating.objects.all()

    def get_serializer_class(self):
        serializer_mappings = {
            'create': RatingCreateSerializer,
            'update': RatingCreateSerializer,
            'partial_update': RatingCreateSerializer,
        }
        return serializer_mappings.get(self.action, RatingGetSerializer)
