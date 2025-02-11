from dataclasses import dataclass


@dataclass
class StatusCodes:
    def __init__(self):
        self.SUCCESS = 200
        self.CREATED = 201
        self.NO_CONTENT = 204
        self.BAD_REQUEST = 400
        self.UNAUTHORIZED = 401
        self.FORBIDDEN = 403
        self.NOT_FOUND = 404
        self.UNPROCESSABLE_ENTITY = 422
        self.INTERNAL_SERVER_ERROR = 500


obj_status_codes = StatusCodes()
StatusCodesDictionary = obj_status_codes.__dict__


@dataclass
class Target:
    def __init__(self):
        self.WHATSAPP = "whatsapp"
        self.SMS = "sms"


obj_target = Target()
TargetDictionary = obj_target.__dict__


@dataclass
class MediaType:
    def __init__(self):
        self.IMAGE = "image"
        self.AUDIO = "audio"
        self.DOCUMENT = "document"
        self.VIDEO = "video"
        self.CONTACT = "contact"


obj_media_type = MediaType()
MediaTypeDictionary = obj_media_type.__dict__


@dataclass
class Platform:
    def __init__(self):
        self.WHATSAPP = "WHATSAPP"
        self.FACEBOOK = "FACEBOOK"
        self.TWILIO = "TWILIO"


obj_platform = Platform()
PlatformDictionary = obj_platform.__dict__


@dataclass
class EmailTypes:
    def __init__(self):
        self.OTP = "OTP"
        self.RESET_PASSWORD = "RESET_PASSWORD"  # nosec
        self.VERIFY_EMAIL = "VERIFY_EMAIL"


obj_email_type = EmailTypes()
EmailTypeDictionary = obj_email_type.__dict__


@dataclass
class DocumentType:
    def __init__(self):
        self.PROPERTY_PAPER = "PROPERTY_PAPER"
        self.PROPERTY_IMAGE = "PROPERTY_IMAGE"
        self.PROPERTY_VIDEO = "PROPERTY_VIDEO"
        self.LOAN_DOCUMENT = "LOAN_DOCUMENT"
        self.OTHER_DOCUMENT = "OTHER_DOCUMENT"


obj_document_type = DocumentType()
DocumentTypeDictionary = obj_document_type.__dict__


@dataclass
class PropertyType:
    def __init__(self):
        self.RESIDENTIAL = "RESIDENTIAL"
        self.COMMERCIAL = "COMMERCIAL"
        self.INDUSTRIAL = "INDUSTRIAL"
        self.AGRICULTURAL = "AGRICULTURAL"
        self.OTHER = "OTHER"


obj_property_type = PropertyType()
PropertyTypeDictionary = obj_property_type.__dict__


@dataclass
class ReturnType:
    def __init__(self):
        self.RENT = "RENT"
        self.APPRECIATION = "APPRICIATION"
        self.OTHER = "OTHER"


obj_return_type = ReturnType()
ReturnTypeDictionary = obj_return_type.__dict__


@dataclass
class BuildingHealth:
    def __init__(self):
        self.EXCELLENT = "EXCELLENT"
        self.GOOD = "GOOD"
        self.AVERAGE = "AVERAGE"
        self.BAD = "BAD"


obj_building_health = BuildingHealth()
BuildingHealthDictionary = obj_building_health.__dict__


@dataclass
class ApprovalStatus:
    def __init__(self):
        self.APPROVE = "APPROVE"
        self.REJECT = "REJECT"

obj_approval_status = ApprovalStatus()
ApprovalStatusDictionary = obj_approval_status.__dict__