from django.contrib import admin
from django.urls import path

from usuarios.views import index
from visitantes.views import visitor_registration

urlpatterns = [
    path("admin/", admin.site.urls),

    path(
        "",
        index,
        name="index",
    ),

    path(
        "visitor_registration/",
        visitor_registration,
        name="visitor_registration"
    )
]
