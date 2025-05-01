from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from contact_us.renderers import UserRenderer
from contact_us.models import ContactUs
from contact_us.serializers import ContactUsSerializer

# Create your views here.

class ContactUsCreateView(APIView):
    renderer_classes = [UserRenderer]  # Supports both JSON and Browsable API

    def post(self, request, format=None):
        serializer = ContactUsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Contact form submitted successfully", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(
            {"errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

