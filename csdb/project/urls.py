"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.views.generic import TemplateView

# Main application index
from project.apps.main.views import IndexView

# Each app added to the project should be configured similarly
from project.apps.main import urls as main_urls

# from project.apps.users import urls as users_api_urls

ec = {"navbar_active_page": "nav-item-login"}

urlpatterns = [
    # Project Apps:
    path("main/", include((main_urls, "main"))),
    # Authentication:
    # TODO: add other authentication views
    path(
        "accounts/login/", auth_views.LoginView.as_view(extra_context=ec), name="login"
    ),
    path(
        "accounts/logout/",
        auth_views.LogoutView.as_view(
            extra_context={"navbar_active_page": "nav-item-logout"}
        ),
        name="logout",
    ),
    path(
        "accounts/password_change/",
        auth_views.PasswordChangeView.as_view(
            extra_context={"navbar_active_page": "nav-item-change-password"}
        ),
        name="password_change",
    ),
    path(
        "accounts/password_change/done/",
        auth_views.PasswordChangeDoneView.as_view(
            extra_context={"navbar_active_page": ""}
        ),
        name="password_change_done",
    ),
    path(
        "accounts/password_reset/",
        auth_views.PasswordResetView.as_view(extra_context=ec),
        name="password_reset",
    ),
    path(
        "accounts/password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(extra_context=ec),
        name="password_reset_done",
    ),
    path(
        "accounts/reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(extra_context=ec),
        name="password_reset_confirm",
    ),
    path(
        "accounts/reset/done/",
        auth_views.PasswordResetCompleteView.as_view(extra_context=ec),
        name="password_reset_complete",
    ),
    # Django Admin:
    path("admin/doc/", include("django.contrib.admindocs.urls")),
    path("admin/", admin.site.urls),
    # Text and xml static files:
    path(
        "robots.txt",
        TemplateView.as_view(template_name="txt/robots.txt", content_type="text/plain"),
    ),
    path(
        "humans.txt",
        TemplateView.as_view(template_name="txt/humans.txt", content_type="text/plain"),
    ),
    # Explicit index view
    path("", IndexView.as_view(), name="index"),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
