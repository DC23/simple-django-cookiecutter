# from django.conf import settings
from django.views import View
from django.shortcuts import render

# Create your views here.


class IndexView(View):
    "Home page view."

    def get(self, request):
        context = {
            "heading": "Home",
            "navbar_active_page": "nav-item-home",
        }
        return render(request, "main/index.html", context)
