from django.urls import path
from charonboat import views

urlpatterns = [
    path("api", views.get_info, name="get_info"),
]