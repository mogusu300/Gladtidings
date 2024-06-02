# core/api.py
from ninja import NinjaAPI, Router
from .models import CustomUser
from .scheme import UserCreateSchema, UserSchema
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth import get_user_model
from .models import Certificate
from .schemas import CertificateSerializer

api = NinjaAPI()

router = Router()

@router.post("/register", response=UserSchema)
def register(request, data: UserCreateSchema):
    user = CustomUser.objects.create_user(
        username=data.username,
        email=data.email,
        password=data.password,
        role=data.role
    )
    return user

class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Override the default queryset to filter certificates by the logged-in user
        user = self.request.user
        return Certificate.objects.filter(user=user)

    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def my_certificates(self, request):
        # Get certificates for the authenticated user
        certificates = self.get_queryset()
        serializer = self.get_serializer(certificates, many=True)
        return Response(serializer.data)

api.add_router("/", router)  # Add the router to the API instance
