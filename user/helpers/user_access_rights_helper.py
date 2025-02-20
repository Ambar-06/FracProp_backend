RIGHTS_SWITCH = {
    "STAFF": [
        "city",
        "state",
        "country",
        "pin_code",
        "type",
        "number_of_floors",
        "number_of_rooms",
        "return_type",
        "govt_allotted_property_id",
        "built_area_in_sqft",
        "area_in_sqft",
        "valuation",
        "delete_images",
    ],
    "ADMIN": "__all__",
}

def get_user_access_rights(user, data):
    if not user.is_admin and not user.is_staff:
        return None, data
    role = "ADMIN" if user.is_admin else "STAFF"
    rights = RIGHTS_SWITCH[role]
    if rights != "__all__":
        data = {key: value for key, value in data.items() if key in rights}
    return rights, data
