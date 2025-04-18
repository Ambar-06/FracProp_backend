from common.helpers.constants import DocumentTypes
from property.models.property import Property
from property.models.property_data_and_document import PropertyRelatedDataAndDocument
from property.models.property_valuation_history import PropertyValuationHistory
from property.models.user_property_amount import UserPropertyAmount
from property.models.user_property_stake import UserPropertyStake


def update_property(uuid, data, image_files=[]):
    property = Property.objects.filter(uuid=uuid).first()
    property.name = data.get("name") or property.name
    property.address = data.get("address") or property.address
    property.description = data.get("description") or property.description
    property.city = data.get("city") or property.city
    property.state = data.get("state") or property.state
    property.country = data.get("country") or property.country
    property.amenities = data.get("amenities") or property.amenities
    property.return_type = data.get("return_type") or property.return_type
    property.type = data.get("type") or property.type
    property.number_of_floors = (
        data.get("number_of_floors") or property.number_of_floors
    )
    property.number_of_rooms = data.get("number_of_rooms") or property.number_of_rooms
    property.built_area_in_sqft = (
        data.get("built_area_in_sqft") or property.built_area_in_sqft
    )
    property.area_in_sqft = data.get("area_in_sqft") or property.area_in_sqft
    property.latitude = data.get("latitude") or property.latitude
    property.longitude = data.get("longitude") or property.longitude
    property.has_loan = (
        data.get("has_loan") if data.get("has_loan") is not None else property.has_loan
    )
    property.is_verified = data.get("is_verified") or property.is_verified
    property.is_approved = data.get("is_approved") or property.is_approved
    property.is_active = data.get("is_active") or property.is_active
    property.other_details = data.get("other_details") or property.other_details
    property.save()
    if data.get("valuation") is not None:
        update_property_valuation(property, data.get("valuation"))
    add_or_update_property_images(data, image_files, property)
    return property

def update_property_valuation(property, valuation):
    if property.valuation != valuation:
        property.valuation = valuation
        property.save()
        PropertyValuationHistory.objects.create(valuation=valuation, property=property)
        user_property_amount_data_qs = UserPropertyAmount.objects.filter(
            property=property
        )
        for user_property_amount in user_property_amount_data_qs:
            user_property_stake = UserPropertyStake.objects.filter(
                user=user_property_amount.user, property=property
            ).first()
            investment_change = calculate_percentage_amount_for_current_valuation(
                valuation, user_property_stake.stake_in_percent
            )
            if investment_change > user_property_amount.total_amount:
                difference =  investment_change - user_property_amount.total_amount
                total_profit = user_property_amount.total_profit or 0
                user_property_amount.total_profit = total_profit + difference
                user_property_amount.total_amount += difference
            else:
                difference = user_property_amount.total_amount - investment_change
                total_loss = user_property_amount.total_loss or 0
                user_property_amount.total_loss = total_loss + difference
                user_property_amount.total_amount -= difference
            print(difference, "difference")
            print(user_property_amount.total_amount, "total_amount")
            user_property_amount.save()
        return True
    return False

def calculate_percentage_amount_for_current_valuation(valuation, stake_in_percent):
    return (valuation * stake_in_percent) / 100

def add_or_update_property_images(data, image_files, property):
    for image in data.get("delete_images", []):
        PropertyRelatedDataAndDocument.objects.filter(
            property=property, document=image
        ).update(is_deleted=True)
    for image in image_files:
        PropertyRelatedDataAndDocument.objects.create(
            property=property,
            document=image,
            document_type=DocumentTypes().PROPERTY_IMAGE,
        )
    return True
