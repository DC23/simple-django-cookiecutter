# from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render

# Create your views here.


class LoremView(LoginRequiredMixin, View):
    "View to test the page scrolling behaviour for large body content."

    def get(self, request):
        context = {
            "navbar_active_page": "nav-item-lorem",
        }
        return render(request, "main/lorem.html", context)
