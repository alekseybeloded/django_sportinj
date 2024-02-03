from .models import Team, Player, Injury
from rest_framework import viewsets
from .serializers import TeamSerializer, PlayerSerializer, InjurySerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class InjuryViewSet(viewsets.ModelViewSet):
    queryset = Injury.objects.all()
    serializer_class = InjurySerializer
