from client.models import ClientModel
from client.serializers import ClientSerializer
from util.views import CassandraModelViewSet


class ClientViewSet(CassandraModelViewSet):
    queryset = ClientModel.objects.all()
    serializer_class = ClientSerializer
    filterset_fields = ['name', 'last_name']
