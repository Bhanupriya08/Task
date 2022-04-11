from django.urls import include, re_path
from django.urls import re_path
from rest_framework.routers import DefaultRouter
from .views import *

app_name = "fibo"

router = DefaultRouter()
router.register(r'', FibonnaciView, "result")



urlpatterns = [
    re_path(r'result/', include(router.urls)),
]