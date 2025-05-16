from django.shortcuts import render
from rest_framework.views import APIView
from sparky_utils.response import service_response

# Create your views here.


class Root(APIView):

    def get(self, request, *args, **kwargs):
        return service_response(
            data={}, status="success", status_code=200, message="Welcome"
        )
