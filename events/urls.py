from django.urls import path

from .views import (
    event_list,
    event_detail,
    sign_up,
    login,
    register_event,
    my_registrations,
    cancel_registration
)


urlpatterns = [

    # Event APIs
    path('events/', event_list),
    path('events/<int:id>/', event_detail),

    # Registration APIs
    path('registration/<int:id>/', register_event),
    path('my-registrations/', my_registrations),
    path('registration/<int:id>/cancel/', cancel_registration),

    # Authentication APIs
    path('signup/', sign_up),
    path('login/', login),
]