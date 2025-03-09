import pyotp 
import qrcode 

class TwoFactorAuthentication:
    def __init__(self):
        pass

    def get_key(self):
        return pyotp.random_base32()

    def generate_totp(self, user_name):
        key = self.get_key()
        return pyotp.totp.TOTP(key).provisioning_uri(name=str(user_name), issuer_name="FracProp"), key

    def generate_qr_code(self, user_name):
        uri, key = self.generate_totp(user_name)
        path = f"media/uploads/qr_auth_for_{user_name}.png"
        qrcode.make(uri).save(path) 
        totp_qr = pyotp.TOTP(key)
        return totp_qr, key, path
    
    def verify_totp(self, key, token):
        totp = pyotp.TOTP(key)
        return totp.verify(token)