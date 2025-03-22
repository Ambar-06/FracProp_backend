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
class Targets:
    def __init__(self):
        self.WHATSAPP = "whatsapp"
        self.SMS = "sms"


obj_target = Targets()
TargetsDictionary = obj_target.__dict__


@dataclass
class MediaTypes:
    def __init__(self):
        self.IMAGE = "image"
        self.AUDIO = "audio"
        self.DOCUMENT = "document"
        self.VIDEO = "video"
        self.CONTACT = "contact"


obj_media_type = MediaTypes()
MediaTypesDictionary = obj_media_type.__dict__


@dataclass
class Platforms:
    def __init__(self):
        self.WHATSAPP = "WHATSAPP"
        self.FACEBOOK = "FACEBOOK"
        self.TWILIO = "TWILIO"


obj_platform = Platforms()
PlatformsDictionary = obj_platform.__dict__


@dataclass
class EmailTypes:
    def __init__(self):
        self.OTP = "OTP"
        self.RESET_PASSWORD = "RESET_PASSWORD"  # nosec
        self.VERIFY_EMAIL = "VERIFY_EMAIL"


obj_email_type = EmailTypes()
EmailTypesDictionary = obj_email_type.__dict__


@dataclass
class DocumentTypes:
    def __init__(self):
        self.PROPERTY_PAPER = "PROPERTY_PAPER"
        self.PROPERTY_IMAGE = "PROPERTY_IMAGE"
        self.PROPERTY_VIDEO = "PROPERTY_VIDEO"
        self.LOAN_DOCUMENT = "LOAN_DOCUMENT"
        self.PROPERTY_DOCUMENT = "PROPERTY_DOCUMENT"
        self.OTHER_DOCUMENT = "OTHER_DOCUMENT"


obj_document_type = DocumentTypes()
DocumentTypesDictionary = obj_document_type.__dict__

@dataclass
class RentalAreaTypes:
    def __init__(self):
        self.ROOM = "ROOM"
        self.FLAT = "FLAT"
        self.HOUSE = "HOUSE"
        self.OTHER = "OTHER"
        self.COMMERCIAL = "COMMERCIAL"

obj_rental_area_type = RentalAreaTypes()
RentalAreaTypesDictionary = obj_rental_area_type.__dict__

@dataclass
class PropertyTypes:
    def __init__(self):
        self.RESIDENTIAL = "RESIDENTIAL"
        self.COMMERCIAL = "COMMERCIAL"
        self.INDUSTRIAL = "INDUSTRIAL"
        self.AGRICULTURAL = "AGRICULTURAL"
        self.OTHER = "OTHER"


obj_property_type = PropertyTypes()
PropertyTypesDictionary = obj_property_type.__dict__


@dataclass
class ReturnTypes:
    def __init__(self):
        self.RENT = "RENT"
        self.APPRECIATION = "APPRICIATION"
        self.OTHER = "OTHER"


obj_return_type = ReturnTypes()
ReturnTypesDictionary = obj_return_type.__dict__


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


@dataclass
class TransactionTypes:
    def __init__(self):
        self.DEPOSIT = "DEPOSIT"
        self.WITHDRAWAL = "WITHDRAWAL"

obj_transaction_type = TransactionTypes()
TransactionTypesDictionary = obj_transaction_type.__dict__


@dataclass
class JobTypes:
    def __init__(self):
        self.FULL_TIME = "FULL_TIME"
        self.PART_TIME = "PART_TIME"
        self.CONTRACT = "CONTRACT"
        self.INTERN = "INTERN"
        self.TEMPORARY = "TEMPORARY"
        self.VOLUNTEER = "VOLUNTEER"
        self.FREELANCE = "FREELANCE"

obj_job_type = JobTypes()
JobTypesDictionary = obj_job_type.__dict__

@dataclass
class JobDepartments:
    def __init__(self):
        self.TECHNOLOGY = "TECHNOLOGY"
        self.MARKETING = "MARKETING"
        self.SALES = "SALES"
        self.CUSTOMER_SERVICE = "CUSTOMER_SERVICE"
        self.OPERATIONS = "OPERATIONS"
        self.HUMAN_RESOURCES = "HUMAN_RESOURCES"
        self.FINANCE = "FINANCE"
        self.LEGAL = "LEGAL"
        self.REAL_ESTATE = "REAL_ESTATE"
        self.OTHER = "OTHER"

obj_job_department = JobDepartments()
JobDepartmentsDictionary = obj_job_department.__dict__