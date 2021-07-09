"""car_booking_api URL Configuration
"""
from django.conf.urls import url, re_path, include
from django.contrib import admin
from rest_framework import routers, permissions
import authentication.urls as auth_urls
import api.urls as api_urls
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)
from rest_auth.views import (LogoutView, PasswordChangeView)


from authentication.views import (
    #     RegisterUserView,
    VerifyEmailView,
    SendVerificationLinkView,
    #     UserLoginView,
    PasswordResetView, PasswordResetConfirmView
)
# DRF - YASG
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://3dservices.co.ug/pages.php?page=vehicles",
        contact=openapi.Contact(email="info@3dservices.co.ug"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    # Default route
    path('', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),

    # Admin route
    url(r'^admin/', admin.site.urls),

    # accounts
    path(r'token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # jwt : User a Refresh Token to refresh the Access Token
    path(r'token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


    # Verifies email for successfull Registration
    path(
        r'verify-email/',
        VerifyEmailView.as_view(),
        name='verify-email'
    ),

    # Resends email verification link for successfull Registration
    path(
        r'verification-link/',
        SendVerificationLinkView.as_view(),
        name='email-verification-link'
    ),

    # URLs that do not require a session or valid token
    path(r'password/reset/', PasswordResetView.as_view(),
         name='rest_password_reset'),
    path(r'password/reset/confirm/', PasswordResetConfirmView.as_view(),
         name='rest_password_reset_confirm'),



    # URLs that require a user to be logged in with a valid session / token.
    path(r'logout/', LogoutView.as_view(), name='rest_logout'),
    path(r'password/change/', PasswordChangeView.as_view(),
         name='rest_password_change'),


    # User Routes
    path('drivers/', include(auth_urls.driver_urls)),
    path('passengers/', include(auth_urls.passenger_urls)),
    path('systemadmins/', include(auth_urls.system_admin_urls)),
    path('fleetmanagers/', include(auth_urls.fleet_manager_urls)),
    # TD: to add a route for user

    # api routes
    path('vehicles/', include(api_urls.vehicle_urls)),
    path('blacklists/', include(api_urls.blacklist_urls)),
    path('branches/', include(api_urls.branch_urls)),
    path('departments/', include(api_urls.department_urls)),
    path('directorates/', include(api_urls.directorate_urls)),
    path('driverblacklists/', include(api_urls.driver_blacklist_urls)),
    path('organisationdrivers/', include(api_urls.organisation_driver_urls)),
    path('organisationfleetmanagers/',
         include(api_urls.organisation_fleet_manager_urls)),
    path('organisationvehicles/', include(api_urls.organisation_vehicle_urls)),
    path('organisations/', include(api_urls.organisation_urls)),
    path('passengerblacklists/', include(api_urls.passenger_blacklist_urls)),
    path('projects/', include(api_urls.project_urls)),
    path('stations/', include(api_urls.station_urls)),
    path('trips/', include(api_urls.trip_urls)),
    path('passengertrips/', include(api_urls.passenger_trip_urls)),
    path('drivertrips/', include(api_urls.driver_trip_urls)),
    path('fleetmanagertrips/', include(api_urls.fleet_manager_trip_urls)),
    path('projectvehicletrips/', include(api_urls.project_vehicle_deploy_urls)),

    # drf-yasg Routes
    path('docs/swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('docs/redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),


]
