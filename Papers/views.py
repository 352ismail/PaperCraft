from rest_framework import viewsets
from .models import Paper
from .serializers import PaperSerializer

# Create your views here.

class PaperView(viewsets.ModelViewSet):
    queryset = Paper.objects.all()
    serializer_class = PaperSerializer