import requests
import  json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import redirect


class STKPushCallBackAPIView(APIView):
    """
    This is where safaricom will post our callbacks then we forward them to respective server.
    """
    def post(self, request, *args, **kwargs):
        if request.data:
            print("posted data is as follows;", request.data)
            api_url = "http://shopyangu.com:8000/f9ec75d9874ae9b88093158318796b44c7131735/callbacks/stk-push/"
            json_request = request.data
            response = requests.post(url=api_url, json=json_request)
            the_response = json.loads(response.text)

        else:
            # not sure how we endup here
            print("no post data")

        message = {
            "ResultCode": 0,
            "ResultDesc": "The service was accepted successfully",
            "ThirdPartyTransID": "1234567890"
        }
        return Response(message, status=status.HTTP_200_OK)


class B2CTimeOutAPIView(APIView):
    """
    this is where Safaricom post the timeout then we forward it to out local server
    """

    def post(self, request, *args, **kwargs):
        if request.data:
            print("posted data is as follows;", request.data)
            api_url = "http://shopyangu.com:8000/f9ec75d9874ae9b88093158318796b44c7131735/callbacks/b2c-timeout/"
            json_request = request.data
            response = requests.post(url=api_url, json=json_request)
            the_response = json.loads(response.text)
        else:
            print("no post data")
        
        message = {
            "ResultCode": 0,
            "ResultDesc": "The service was accepted successfully",
            "ThirdPartyTransID": "1234567890"
        }
        return Response(message, status=status.HTTP_200_OK)


class B2CResultAPIView(APIView):
    def post(self, request, *args, **kwargs):
        if request.data:
            print("posted data is as follows;", request.data)
            api_url = "http://shopyangu.com:8000/f9ec75d9874ae9b88093158318796b44c7131735/safaricom-callbacks/b2c-results/"
            json_request = request.data
            response = requests.post(url=api_url, json=json_request)
            the_response = json.loads(response.text)
        else:
            print("no post data")
        
        message = {
            "ResultCode": 0,
            "ResultDesc": "The service was accepted successfully",
            "ThirdPartyTransID": "1234567890"
        }
        return Response(message, status=status.HTTP_200_OK)



class SMSCallbackAPIView(APIView):
    def post(self, request, *args, **kwargs):
        if request.data:
            print("posted data is as follows;", request.data)
            api_url = "http://shopyangu.com:8000/f9ec75d9874ae9b88093158318796b44c7131735/callbacks/sms-delivery-report-callback/"
            json_request = request.data
            response = requests.post(url=api_url, json=json_request)
            the_response = json.loads(response.text)
        
        else:
            print("no post data")
        
        message = {
            "ResultCode": 0,
            "ResultDesc": "The service was accepted successfully",
            "ThirdPartyTransID": "1234567890"
        }
        return Response(message, status=status.HTTP_200_OK)



def to_shopyangu(request):
    the_url = "http://shopyangu.com:8000/"
    return redirect(the_url)
