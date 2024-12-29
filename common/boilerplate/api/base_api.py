import typing as _
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from common.helpers.constants import StatusCodes


T = _.TypeVar("T")

"""
This class is used for base api view
This class is inherited from APIView
Fields:
Methods:
    success: This method is used to return success response
    error: This method is used to return error response
    validation_failed: This method is used to return validation failed response
    error_message: This method is used to return error message response
    error_message_without_data: This method is used to return error message without data response
    no_content: This method is used to return no content response
"""


class ResponseOrError:
    def __init__(self):
        pass

    def success(
        self, data: T, code=StatusCodes().SUCCESS, msg: _.Optional[str] = None
    ) -> Response:
        return Response(
            {
                "success": True,
                "code": code,
                "data": data,
                "message": msg,
            },
            status=code,
        )

    def error(self, errors: T, status_code: int) -> Response:
        return Response(
            {"success": False, "code": status_code, "errors": errors},
            status=status_code,
        )

    def validation_failed(self, **kwargs) -> Response:
        return self.error(kwargs, StatusCodes().UNPROCESSABLE_ENTITY)

    def error_message(
        self, msg: str, code: int, data: _.Optional[dict] = None
    ) -> Response:
        return Response(
            {"success": False, "code": code, "message": msg, "data": data}, status=code
        )

    def error_message_without_data(self, msg: str, code: int) -> Response:
        return Response(
            {
                "success": False,
                "code": code,
                "message": msg,
            },
            status=code,
        )

    def no_content(self) -> Response:
        return Response(status=StatusCodes().NO_CONTENT)

    def get_response_or_error(self, response : dict) -> tuple:
        response_keys = ["response_data", "errors"]
        resp = None
        code = None
        for key, value in response.items():
            if key in response_keys:
                resp = value
            else:
                code = value
        return resp, code

class BaseAPIView(APIView, ResponseOrError):
    ...
    

class BaseModelViewSet(ModelViewSet, ResponseOrError):
    ...