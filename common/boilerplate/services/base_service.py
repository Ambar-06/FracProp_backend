import typing as _

from common.helpers.constants import StatusCodes

T = _.TypeVar("T")


class BaseService:
    def ok(self, data: T, status_code: _.Optional[int] = StatusCodes().SUCCESS):
        return {"response_data": data, "code": status_code}

    def exception(self, errors: T, status_code: int):
        return {"errors": errors, "code": status_code}

    def bad_request(self, message: str):
        return self.exception(message, StatusCodes().BAD_REQUEST)

    def unauthorized(self, message: str):
        return self.exception(message, StatusCodes().UNAUTHORIZED)

    def forbidden(self, message: str):
        return self.exception(message, StatusCodes().FORBIDDEN)

    def not_found(self, message: str):
        return self.exception(message, StatusCodes().NOT_FOUND)

    def validation_failed(self, **kwargs):
        return self.exception(kwargs, StatusCodes().UNPROCESSABLE_ENTITY)
