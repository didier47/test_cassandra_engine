import datetime
import uuid

from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel


class ClientModel(DjangoCassandraModel):
    id = columns.UUID(primary_key=True, default=uuid.uuid4)
    name = columns.Text()
    last_name = columns.Text()
    created_at = columns.DateTime(default=datetime.datetime.now)
