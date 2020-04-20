from django.urls import path

from . import views

app_name = "main"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("lorem", views.LoremView.as_view(), name="lorem"),
    path("debug", views.DebugView.as_view(), name="debug"),
    path("er", views.ErView.as_view(), name="er"),
]
