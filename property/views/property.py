from common.boilerplate.api.base_api import BaseModelViewSet, BaseAPIView
from common.boilerplate.decorators.auth_guard import auth_guard
from common.boilerplate.decorators.validate_request import validate_request
from common.helpers.constants import StatusCodes
from property.serializers.property_serializers import PropertySerializer

from property.services.property_services import PropertyServices


class PropertyView(BaseAPIView):
    def __init__(self):
        self.service = PropertyServices()

    @auth_guard()
    @validate_request()
    def get(self, request, data, *args):
        service_data = self.service.get_service(request, data)
        response, status_code = self.get_response_or_error(service_data)
        return self.success(response, status_code)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return self.success(serializer.data)

    @auth_guard(admin=True)
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
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return self.success(serializer.data, StatusCodes().SUCCESS)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_deleted = True
        instance.save()
        return self.no_content()
