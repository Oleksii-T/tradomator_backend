from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    # Let DRF's default exception handler process the exception first
    response = exception_handler(exc, context)

    # If there's a validation error, wrap it in an "errors" key
    if response is not None and response.status_code == status.HTTP_400_BAD_REQUEST:
        response.data = {"errors": response.data}

    return response
