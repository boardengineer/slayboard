from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'runs', views.RunHistoryViewSet)
router.register(r'floor_results', views.FloorResultsViewSet)
router.register(r'battles', views.BattlesViewSet)
router.register(r'battle_commands', views.BattleCommandsViewSet)
router.register(r'vote_results', views.VoteResultsViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('', include(router.urls)),
    path('floor_result_query', views.FloorResultList.as_view()),
    path('battle_command_query', views.BattleCommandList.as_view()),
    path('vote_result_query', views.VoteResultsList.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]