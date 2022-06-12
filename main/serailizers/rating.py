from rest_framework import serializers

from main.models import Rating
from users.admin import CustomUser


class CurrentCustomerDefault:
    requires_context = True

    def __call__(self, serializer_field):
        return serializer_field.context["request"].user

    def __repr__(self):
        return "%s()" % self.__class__.__name__


class RatingCreateSerializer(serializers.ModelSerializer):
    # customer = serializers.HiddenField(default=CurrentCustomerDefault())
    def to_internal_value(self, data):
        request = self.context.get('request')
        if request.user.role == CustomUser.Role.CUSTOMER:
            data['customer'] = request.user.id
        else:
            raise Exception('Only users with role of customer can rate the service!')
        return super().to_internal_value(data)

    class Meta:
        model = Rating
        fields = ('id', 'company', 'customer','rating', 'comment')


class RatingGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'company', 'customer','rating', 'comment')