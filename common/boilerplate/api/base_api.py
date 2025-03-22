import typing as _

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

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
        self, data: T, code: int = StatusCodes().SUCCESS, msg: _.Optional[str] = None
    ) -> Response:
        """Returns a successful response."""
        if data == {} and len(self.kwargs.items()) == 0:
            data = []
        return Response(
            {
                "success": True,
                "code": code,
                "data": data,
                "message": msg or "",
            },
            status=code,
        )

    def error(self, errors: T, code: int) -> Response:
        """Returns an error response with specified errors."""
        return Response(
            {"success": False, "code": code, "errors": errors},
            status=code,
        )

    def error_message(
        self, msg: str, code: int, data: _.Optional[dict] = None
    ) -> Response:
        """Returns an error response with a message and optional data."""
        return Response(
            {"success": False, "code": code, "message": msg, "data": data},
            status=code,
        )

    def error_message_without_data(self, msg: str, code: int) -> Response:
        """Returns an error response with a message and no data."""
        return Response(
            {
                "success": False,
                "code": code,
                "message": msg,
            },
            status=code,
        )

    def no_content(self) -> Response:
        """Returns a no content response."""
        return Response(status=StatusCodes().NO_CONTENT)

    def get_response_or_error(self, response: dict) -> tuple:
        """
        Extracts response data and status code from a response dictionary.
        Assumes the dictionary has either 'response_data' or 'errors'.
        """
        response_keys = ["response_data", "errors"]
        resp = None
        code = None

        for key, value in response.items():
            if key in response_keys:
                resp = value
            else:
                code = value

        # If no valid response or status code found, return an empty tuple
        return resp or {}, code or StatusCodes().BAD_REQUEST
    
    def response(self, response, code: int) -> Response:
        """Returns a response with the specified response data and status code, based on code condition"""
        if code in [StatusCodes().SUCCESS, StatusCodes().CREATED]:
            return self.success(response, code=code)
        if code == StatusCodes().NO_CONTENT:
            return self.no_content()
        return self.error(response, code=code)


class BaseAPIView(APIView, ResponseOrError):
    """Base API view that includes response helpers from ResponseOrError."""


class BaseModelViewSet(ModelViewSet, ResponseOrError):
    """Base ModelViewSet that includes response helpers from ResponseOrError."""
