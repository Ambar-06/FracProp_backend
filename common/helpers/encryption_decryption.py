import traceback
import logging
import base64
import hashlib
import hmac
from cryptography.fernet import Fernet

from frac_prop import settings

KEYS = {
    (1,): settings.ENCRYPT_KEY1,
    (2,) : settings.ENCRYPT_KEY2,
    (3,) : settings.ENCRYPT_KEY3,
    (4,) : settings.ENCRYPT_KEY4,
    (5,) : settings.ENCRYPT_KEY5
}


def encrypt(pas, serial=1):
    try:
        pas = str(pas)
        key = KEYS.get((serial,), settings.ENCRYPT_KEY1)
        cipher_pass = Fernet(key)
        encrypt_pass = cipher_pass.encrypt(pas.encode("ascii"))
        encrypt_pass = base64.urlsafe_b64encode(encrypt_pass).decode("ascii")
        return encrypt_pass
    except Exception as e:
        logging.getLogger("error_logger").error(traceback.format_exc())
        return None


def decrypt(pas, serial=1):
    try:
        pas = base64.urlsafe_b64decode(pas)
        key = KEYS.get((serial,), settings.ENCRYPT_KEY1)
        cipher_pass = Fernet(key)
        decod_pass = cipher_pass.decrypt(pas).decode("ascii")
        return decod_pass
    except Exception as e:
        logging.getLogger("error_logger").error(traceback.format_exc())
        return None


def generate_hash(string, hash_type="sha256"):
    """
    Generates hex digest of the given string using the provided hashing method

    Currently these hashing methods are supported:
    * sha256
    * md5

    Params
    -------
        string : str
            String to be hashed
        hash_type : str
            type of hashing to use

    Returns
    --------
        str : hexdigest of the string

        OR

        None : if hash_type isn't present
    """
    hash_functions = {
        "sha256": lambda: hashlib.sha256(string.encode()).hexdigest(),
        "md5": lambda: hashlib.md5(string.encode()).hexdigest(), #nosec
    }

    return hash_functions.get(hash_type)() if hash_functions.get(hash_type) else None


def convert_string_to_base64(string: str):
    sample_string_bytes = string.encode("ascii")
    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")
    return base64_string


def convert_base64_to_string(string: base64):
    base64_bytes = string.encode("ascii")
    string_bytes = base64.b64decode(base64_bytes)
    original_string = string_bytes.decode("ascii")
    return original_string


def generate_hmac_256_signature(string: str, secret: str) -> str:
    """
    Generates Hmac 256 signature.
    """
    secret = secret.encode("utf-8")
    string = string.encode("utf-8")
    signature = hmac.new(secret, string, hashlib.sha256).hexdigest()
    return signature