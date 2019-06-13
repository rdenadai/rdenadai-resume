# -*- coding: utf-8 -*-

from django.conf.urls import url
import info.views


urlpatterns = [url(r"^", info.views.index, name="info_view_index")]
