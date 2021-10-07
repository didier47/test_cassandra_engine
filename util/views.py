from django.db.models import QuerySet
from django_cassandra_engine.models import DjangoCassandraQuerySet
from rest_framework.viewsets import ModelViewSet


class CassandraModelViewSet(ModelViewSet):

    def get_queryset(self):
        assert self.queryset is not None, (
                "'%s' should either include a `queryset` attribute, "
                "or override the `get_queryset()` method."
                % self.__class__.__name__
        )

        queryset = self.queryset
        if isinstance(queryset, QuerySet) or isinstance(queryset, DjangoCassandraQuerySet):
            queryset = queryset.all()
        return queryset
