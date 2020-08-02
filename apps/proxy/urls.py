"""
main_home URL Configuration
""" 
from django.urls import path

from .views import (
    STKPushCallBackAPIView, 
    to_shopyangu,
    B2CTimeOutAPIView,
    B2CResultAPIView,
    SMSCallbackAPIView
)


app_name = 'proxy'


urlpatterns = [
    # Callbacks
    path('callbacks/stk-push/', STKPushCallBackAPIView.as_view(),
         name='mpesa_stkpush_callback'),
    path('callbacks/b2c-timeout/', B2CTimeOutAPIView.as_view(),
         name='mpesa_b2c_timeout_callback'),
    path('callbacks/b2c-results/', B2CResultAPIView.as_view(),
         name='mpesa_b2c_result_callback'),
    path('callbacks/sms-callback/', SMSCallbackAPIView.as_view(), name='sms_callback'),
    path('callbacks/to-shopyangu/', to_shopyangu, name='to_shopyangu_view'),
]
