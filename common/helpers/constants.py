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