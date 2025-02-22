from rest_framework import serializers
from common.helpers.constants import ApprovalStatus, ApprovalStatusDictionary


class SingleApprovalRequestFilterSerializer(serializers.Serializer):
    request_id = serializers.UUIDField(required=True)
    action = serializers.ChoiceField(
        required=False, choices=ApprovalStatusDictionary, allow_null=True
    )
    remarks = serializers.CharField(required=False)

    def validate(self, attrs):
        request = self.context.get("request")

        if request and request.method in ["PATCH"] and "action" not in attrs:
            raise serializers.ValidationError(
                {"action": "This field is required for PATCH requests."}
            )

        if attrs.get("action") == ApprovalStatus().REJECT and not attrs.get("remarks"):
            raise serializers.ValidationError(
                {"remarks": "Remarks are required for rejection."}
            )

        return attrs
