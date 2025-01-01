from common.boilerplate.api.base_api import BaseModelViewSet
from common.helpers.constants import StatusCodes
from property.serializers.property_serializers import PropertySerializer
from property.models.property import Property
from rest_framework import filters


class PropertyView(BaseModelViewSet):
    serializer_class = PropertySerializer
    queryset = Property.objects.all().order_by("-created_at")
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name", "address", "description"]
    ordering_fields = ["name", "address", "description", "created_at", "updated_at"]
    ordering = ["-created_at"]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return self.success(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return self.success(serializer.data)

    def create(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        serializer = PropertySerializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return self.success(serializer.data, StatusCodes().CREATED)

    def update(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        data["updated_by"] = user.id
        instance = self.get_object()
        serializer = PropertySerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return self.success(serializer.data, StatusCodes().SUCCESS)
        return self.bad_request(serializer.errors)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        return self.no_content()
