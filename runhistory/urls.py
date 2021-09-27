from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'runs', views.RunHistoryViewSet)
router.register(r'floor_results', views.FloorResultsViewSet)
router.register(r'battles', views.BattlesViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]