from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

def validate_user_password(password, user=None):
    try:
        validate_password(password, user=user)
        print("Password is valid.")
        return True
    except ValidationError as e:
        print("Password validation failed:")
        for error in e:
            print(f"- {error}")
        return False