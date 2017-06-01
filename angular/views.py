import os
from django.shortcuts import render

from django.conf import settings
from django.http import HttpResponse, Http404
from django.views.generic import View


class HomeTemplateView(View):
    def get(self, request, item=None, *args, **kwargs):
        return render(request, "angular/" + item + ".html", {})

class AccountTemplateView(View):
    def get(self, request, item=None, *args, **kwargs):
        return render(request, "account/" + item + ".html", {})

        