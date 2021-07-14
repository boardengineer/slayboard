from django.http import HttpResponse
from django.template import loader

from rest_framework import viewsets
from .serializers import STSRunSerializer
from .models import STSRun

def index(request):
    run_list = STSRun.objects.all()
    template = loader.get_template('index.html')
    context = {
        'run_list': run_list,
    }
    return HttpResponse(template.render(context, request))

class RunHistoryViewSet(viewsets.ModelViewSet):
    queryset = STSRun.objects.all()
    serializer_class = STSRunSerializer