from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

from .models import Events, Registration
from .serializers import (
    Eventserializer,
    Userserializer,
    Loginserializer,
    Registrationserializer
)


# =========================
# EVENT LIST API
# =========================

@api_view(['GET'])
def event_list(request):
    events = Events.objects.all()

    serializer = Eventserializer(
        events,
        many=True
    )

    return Response(serializer.data)


# =========================
# EVENT DETAIL API
# =========================

@api_view(['GET'])
def event_detail(request, id):
    event = Events.objects.get(id=id)

    serializer = Eventserializer(event)

    return Response(serializer.data)


# =========================
# REGISTER EVENT API
# =========================

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def register_event(request, id):
    event = Events.objects.get(id=id)

    registration = Registration.objects.create(
        user=request.user,
        event=event
    )

    serializer = Registrationserializer(
        registration
    )

    return Response({
        "message": "Event registered successfully",
        "registration": serializer.data
    })


# =========================
# MY REGISTRATIONS API
# =========================

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_registrations(request):
    registrations = Registration.objects.filter(
        user=request.user
    )

    serializer = Registrationserializer(
        registrations,
        many=True
    )

    return Response(serializer.data)


# =========================
# CANCEL REGISTRATION API
# =========================

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def cancel_registration(request, id):
    registration = Registration.objects.get(
        id=id,
        user=request.user
    )

    registration.delete()

    return Response({
        "message": "Registration cancelled successfully"
    })


# =========================
# SIGN UP API
# =========================

@api_view(['POST'])
def sign_up(request):
    serializer = Userserializer(
        data=request.data
    )

    if serializer.is_valid():
        serializer.save()

        return Response({
            "message": "User created successfully"
        })

    return Response(
        serializer.errors,
        status=400
    )


# =========================
# LOGIN API
# =========================

@api_view(['POST'])
def login(request):
    serializer = Loginserializer(
        data=request.data
    )

    if serializer.is_valid():
        user = serializer.validated_data['user']

        token, created = Token.objects.get_or_create(
            user=user
        )

        return Response({
            "message": "Login successful",
            "Token": token.key
        })

    return Response(
        serializer.errors,
        status=400
    )