from rest_framework import serializers

from common.helpers.constants import EmailTypesDictionary
from notification.models.email_template import EmailTemplate

class TemplateSerializer(serializers.Serializer):
    template_type = serializers.ChoiceField(choices=EmailTypesDictionary, required=True)
    is_hidden = serializers.BooleanField(required=False, allow_null=True, default=False)
    template = serializers.CharField(required=True)

class TemplateViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailTemplate
        fields = "__all__"