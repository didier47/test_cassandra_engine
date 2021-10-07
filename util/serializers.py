from cassandra.cqlengine import columns
from rest_framework import fields
from rest_framework.serializers import ModelSerializer

from util.fields import Email


class CassandraModelSerializer(ModelSerializer):
    serializer_field_mapping = {
        columns.Boolean: fields.BooleanField,
        columns.Date: fields.DateField,
        columns.DateTime: fields.DateTimeField,
        columns.Decimal: fields.DecimalField,
        columns.Duration: fields.DurationField,
        Email: fields.EmailField,
        columns.Float: fields.FloatField,
        columns.Integer: fields.IntegerField,
        columns.Text: fields.CharField,
        columns.Time: fields.TimeField,
        columns.UUID: fields.UUIDField,
    }
