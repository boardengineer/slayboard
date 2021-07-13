from django.http import HttpResponse

from rest_framework import viewsets
from .serializers import STSRunSerializer
from .models import STSRun

def index(request):
    return HttpResponse("Hello, world. You're at the runhistory index.")

class RunHistoryViewSet(viewsets.ModelViewSet):
    queryset = STSRun.objects.all()
    serializer_class = STSRunSerializer