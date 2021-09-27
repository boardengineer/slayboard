from django.http import HttpResponse
from django.template import loader

from rest_framework import viewsets
from .serializers import STSRunSerializer, FloorResultSerializer, BattleSerializer
from .models import STSRun, FloorResult, Battle

def index(request):
    run_list = STSRun.objects.order_by('-id')[:10]
    template = loader.get_template('index.html')
    context = {
        'run_list': run_list,
    }
    return HttpResponse(template.render(context, request))

class RunHistoryViewSet(viewsets.ModelViewSet):
    queryset = STSRun.objects.all()
    serializer_class = STSRunSerializer


class FloorResultsViewSet(viewsets.ModelViewSet):
    queryset = FloorResult.objects.all()
    serializer_class = FloorResultSerializer

class BattlesViewSet(viewsets.ModelViewSet):
    queryset = Battle.objects.all()
    serializer_class = BattleSerializer