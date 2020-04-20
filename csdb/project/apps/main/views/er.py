from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render


class ErView(LoginRequiredMixin, View):
    " Displays the latest Entity-Relationship diagrams. "

    def get(self, request):
        context = {
            "heading": "Latest Entity-Relationship Diagrams",
            "navbar_active_page": "nav-item-er",
        }
        return render(request, "main/er.html", context)
