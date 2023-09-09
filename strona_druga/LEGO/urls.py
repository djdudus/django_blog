from django.urls import path
from . import views

from .views import SetDetailView

urlpatterns = [
    path("", views.lego, name="lego"),
    path("set/<str:pk>/", SetDetailView.as_view(), name="set-detail"),
]
