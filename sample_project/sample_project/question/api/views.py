from rest_framework import viewsets
from sample_project.question import models
from . import serializers


class CoreValueViewSet(viewsets.ModelViewSet):
    """
    ViewSet to perform CRUD operation on the CoreValue model.

    create: To create a core value.

    list: Lists all the core values.

    retrieve: To get a core value data.

    update: To update all core value data fields.

    partial_update: To update one or more core value data fields.

    destroy: To delete a core value.
    """
    queryset = models.CoreValue.objects.all()
    serializer_class = serializers.CoreValueSerializer
