from client.models import ClientModel
from util.serializers import CassandraModelSerializer


class ClientSerializer(CassandraModelSerializer):
    class Meta:
        model = ClientModel
        fields = '__all__'
        read_only_fields = ['id', 'created_at']
