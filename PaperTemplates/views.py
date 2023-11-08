from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import PaperTemplate
from .serializers import PaperTemplateSerializer
# Create your views here.


class PaperTemplateViewset(viewsets.ModelViewSet):
    queryset = PaperTemplate.objects.all()
    serializer_class = PaperTemplateSerializer