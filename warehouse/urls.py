from django.contrib import admin
from django.urls import path, include
from inventory.views import DashboardView, LoginView, LogoutView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/login/", LoginView.as_view(), name="login"),
    path("accounts/logout/", LogoutView.as_view(), name="logout"),
    path("", DashboardView.as_view(), name="dashboard"),
    path("inventory/", include("inventory.urls")),
]
