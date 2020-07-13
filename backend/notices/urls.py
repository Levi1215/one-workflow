# -*- coding: utf-8 -*-
# author: itimor


from django.conf.urls import url
from rest_framework import routers
from notices.views import NoticeViewSet, MailBotViewSet

router = routers.DefaultRouter()

router.register(r'notice', NoticeViewSet)
router.register(r'mail', MailBotViewSet)

urlpatterns = [
]

urlpatterns += router.urls
