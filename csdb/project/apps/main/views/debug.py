from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render


class DebugView(LoginRequiredMixin, View):
    " Development view for displaying debug information "

    def get(self, request):
        context = {
            "heading": "Debug Info",
            "remote_addr": request.META["REMOTE_ADDR"],
            "navbar_active_page": "nav-item-debug",
            # "extra_content": "",
        }
        return render(request, "main/debug.html", context)
