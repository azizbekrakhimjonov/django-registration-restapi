from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.contrib import admin
from django.urls import re_path
from . import views

schema_view = get_schema_view(
    openapi.Info(
        title="Registration API",
        default_version='v1',
        description="API documentation for the register app",
        terms_of_service="https://t.me/calibr_i",
        contact=openapi.Contact(email="azizbekrahimjonov571@gmail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    re_path('admin/', admin.site.urls),

    re_path('login', views.login),
    re_path('signup', views.signup),
    re_path('test_token', views.test_token)
]
