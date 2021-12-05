from django.http import HttpResponse
from django.template import loader

from rest_framework import viewsets, generics
from .serializers import STSRunSerializer, FloorResultSerializer, BattleSerializer, BattleCommandSerializer, VoteResultSerializer
from .models import STSRun, FloorResult, Battle, BattleCommand, VoteResult

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


class BattleCommandsViewSet(viewsets.ModelViewSet):
    queryset = BattleCommand.objects.all()
    serializer_class = BattleCommandSerializer


class VoteResultsViewSet(viewsets.ModelViewSet):
    queryset = VoteResult.objects.all()
    serializer_class = VoteResultSerializer


class FloorResultList(generics.ListAPIView):
    serializer_class = FloorResultSerializer

    def get_queryset(self):
        run = self.request.query_params.get('run')
        floor_num  = self.request.query_params.get('floor_num')
        queryset = FloorResult.objects.filter(floor_num=floor_num, run=run)
        return queryset


class BattleCommandList(generics.ListAPIView):
    serializer_class = BattleCommandSerializer

    def get_queryset(self):
        floor_result = self.request.query_params.get('floor_result')
        queryset = BattleCommand.objects.filter(floor_result=floor_result)
        return queryset


class VoteResultsList(generics.ListAPIView):
    serializer_class = VoteResultSerializer

    def get_queryset(self):
        run = self.request.query_params.get('run')
        floor_num  = self.request.query_params.get('floor_num')
        index = self.request.query_params.get('index')
        queryset = VoteResult.objects.filter(floor_num=floor_num, run=run, index=index)
        return queryset