from property.models.property import Property
from property.models.property_valuation_history import PropertyValuationHistory


def update_property(uuid, data):
    property = Property.objects.filter(uuid=uuid).first()
    property.name = data.get("name") or property.name
    property.address = data.get("address") or property.address
    property.description = data.get("description") or property.description
    property.type = data.get("type") or property.type
    property.number_of_floors = (
        data.get("number_of_floors") or property.number_of_floors
    )
    property.built_area_in_sqft = (
        data.get("built_area_in_sqft") or property.built_area_in_sqft
    )
    property.area_in_sqft = data.get("area_in_sqft") or property.area_in_sqft
    property.latitude = data.get("latitude") or property.latitude
    property.longitude = data.get("longitude") or property.longitude
    property.has_loan = data.get("has_loan") or property.has_loan
    property.is_verified = data.get("is_verified") or property.is_verified
    property.is_approved = data.get("is_approved") or property.is_approved
    property.is_active = data.get("is_active") or property.is_active
    property.other_details = data.get("other_details") or property.other_details
    property.save()
    update_property_valuation(property, data.get("valuation"))
    return property


def update_property_valuation(property, valuation):
    if property.valuation != valuation:
        property.valuation = valuation
        property.save()
        PropertyValuationHistory.objects.create(valuation=valuation, property=property)
        return True
    return False
