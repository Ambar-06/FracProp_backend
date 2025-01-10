from rest_framework import serializers

from common.helpers.constants import PlatformDictionary

class GetUserDetailSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    platform = serializers.ChoiceField(choices=list(PlatformDictionary.values()))

class SingleUserSerializer(serializers.Serializer):
    user_id = serializers.UUIDField(required=True)
    is_active = serializers.BooleanField(required=False, allow_null=True)