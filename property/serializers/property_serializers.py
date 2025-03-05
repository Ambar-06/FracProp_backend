import json
from rest_framework import serializers

from common.helpers.constants import (
    BuildingHealthDictionary,
    DocumentType,
    PropertyTypeDictionary,
    ReturnTypeDictionary,
)
from property.models.property import Property
from property.models.property_data_and_document import PropertyRelatedDataAndDocument
from property.models.user_property_amount import UserPropertyAmount
from property.models.user_property_stake import UserPropertyStake
from property.serializers.property_valuation_history_serializers import (
    PropertyValuationHistorySerializer,
)
from user.models.user import User


class PropertySerializer(serializers.ModelSerializer):

    valuation_history = serializers.SerializerMethodField("get_valuation_history")
    property_images = serializers.SerializerMethodField("get_property_images")
    user_investments = serializers.SerializerMethodField("get_user_investments")
    user_percentage_ownership = serializers.SerializerMethodField(
        "get_user_percentage_ownership_details"
    )
    buyable = serializers.SerializerMethodField("get_buyable")
    favorite = serializers.SerializerMethodField("get_favorites")
    avg_rating = serializers.SerializerMethodField("get_avg_rating")

    class Meta:
        model = Property
        fields = (
            "uuid",
            "name",
            "address",
            "city",
            "state",
            "country",
            "pin_code",
            "description",
            "type",
            "govt_allotted_property_id",
            "number_of_floors",
            "number_of_rooms",
            "return_type",
            "built_area_in_sqft",
            "area_in_sqft",
            "sold_percentage",
            "latitude",
            "longitude",
            "investment_lock_in_period_in_months",
            "valuation",
            "has_loan",
            "is_verified",
            "is_approved",
            "is_active",
            "other_details",
            "amenities",
            "valuation_history",
            "property_images",
            "user_investments",
            "user_percentage_ownership",
            "buyable",
            "favorite",
            "avg_rating",
        )

    def get_avg_rating(self, obj):
        if obj.property_average_rating.first():
            return obj.property_average_rating.first().average_rating
        return 0.0


    def get_favorites(self, obj):
        request = self.context.get("request")
        if request:
            user = User.objects.filter(uuid=request.user.get("uuid")).first()
            if user:
                return user.wishlist.filter(property=obj, is_active=True).exists()
        return False

    def get_user_percentage_ownership_details(self, obj):
        request = self.context.get("request")
        if request:
            user = User.objects.filter(uuid=request.user.get("uuid")).first()
            user_property_amount = UserPropertyStake.objects.filter(
                user=user, property=obj
            ).first()
            if user_property_amount:
                return {
                    "stake_in_percent": user_property_amount.stake_in_percent,
                }
        return {}

    def get_property_images(self, obj):
        return PropertyRelatedDataAndDocument.objects.filter(
            property=obj, document_type=DocumentType().PROPERTY_IMAGE
        ).values_list("document", flat=True)

    def get_valuation_history(self, obj):
        property_val_history = obj.valuation_history.all().order_by("-created_at")[:10]
        return PropertyValuationHistorySerializer(property_val_history, many=True).data

    def get_user_investments(self, obj):
        request = self.context.get("request")
        if request:
            user = User.objects.filter(uuid=request.user.get("uuid")).first()
            user_property_amount = UserPropertyAmount.objects.filter(
                user=user, property=obj
            ).first()
            if user_property_amount:
                return {
                    "total_amount": user_property_amount.total_amount,
                    "total_investment": user_property_amount.total_investment,
                    "total_withdrawal": user_property_amount.total_withdrawal,
                    "total_profit": user_property_amount.total_profit,
                    "total_loss": user_property_amount.total_loss,
                }
        return {}

    def get_buyable(self, obj):
        buyable_percentage = 100 - obj.sold_percentage if obj.sold_percentage else 100
        return {
            "percentage": buyable_percentage,
            "amount": obj.valuation * (buyable_percentage / 100),
        }


class OtherDetailsSerializer(serializers.Serializer):

    construction_age_in_years = serializers.IntegerField(
        required=True, min_value=0, max_value=100
    )
    building_health = serializers.ChoiceField(
        required=True, choices=BuildingHealthDictionary
    )


class AmenitiesFieldSerializer(serializers.Serializer):

    available = serializers.BooleanField(required=True)
    distance_in_km = serializers.FloatField(required=False, default=0.0)


class AmenitiesSerializer(serializers.Serializer):

    school = AmenitiesFieldSerializer(required=True)
    hospital = AmenitiesFieldSerializer(required=True)
    park = AmenitiesFieldSerializer(required=True)
    shopping_mall = AmenitiesFieldSerializer(required=True)


class PropertyFilterSerializer(serializers.Serializer):

    name = serializers.CharField(required=True)
    address = serializers.CharField(required=True)
    city = serializers.CharField(required=True)
    state = serializers.CharField(required=True)
    country = serializers.CharField(required=True)
    pin_code = serializers.CharField(required=False)
    description = serializers.CharField(required=False)
    type = serializers.ChoiceField(choices=PropertyTypeDictionary, required=True)
    govt_allotted_property_id = serializers.CharField(required=True)
    number_of_floors = serializers.IntegerField(required=True, min_value=0)
    number_of_rooms = serializers.IntegerField(required=True, min_value=0)
    return_type = serializers.ChoiceField(choices=ReturnTypeDictionary, required=True)
    built_area_in_sqft = serializers.FloatField(required=True)
    area_in_sqft = serializers.FloatField(required=True)
    latitude = serializers.FloatField(required=True)
    longitude = serializers.FloatField(required=True)
    investment_lock_in_period_in_months = serializers.IntegerField(required=True)
    valuation = serializers.FloatField(required=True)
    has_loan = serializers.BooleanField(required=False, default=False)
    is_verified = serializers.BooleanField(required=False, default=False)
    is_approved = serializers.BooleanField(required=False, default=False)
    is_active = serializers.BooleanField(required=False, default=True)
    other_details = OtherDetailsSerializer(required=True)
    amenities = AmenitiesSerializer(required=True)
    property_images = serializers.ListField(
        child=serializers.ImageField(), required=True, allow_empty=False
    )

    def to_internal_value(self, data):
        """Convert JSON string fields into Python dictionaries before validation."""
        json_fields = [
            field.name
            for field in Property._meta.fields
            if field.get_internal_type() == "JSONField"
        ]

        for field in json_fields:
            if field in data and isinstance(data[field], str):
                try:
                    data[field] = json.loads(data[field])
                except json.JSONDecodeError:
                    raise serializers.ValidationError({field: "Invalid JSON format"})
        if "property_images" in data:
            value = data["property_images"]
            if not isinstance(value, list):
                raise serializers.ValidationError(
                    "Invalid format. Expected a list of images."
                )

            for file in value:
                if not hasattr(file, "file"):
                    raise serializers.ValidationError(f"Invalid file: {file}.")

        return super().to_internal_value(data)
