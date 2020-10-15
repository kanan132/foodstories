from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet
from .serializers import SubscribeSerializer
from stories.models import Subscribe

class SubscribeAPI(CreateAPIView):
    queryset = Subscribe.objects.all()
    serializer_class = SubscribeSerializer
