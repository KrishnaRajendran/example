from rest_framework import viewsets
from sample_project.project import models
from . import serializers


class ClientViewSet(viewsets.ModelViewSet):
    """
    ViewSet to perform CRUD operation on the Client model.

    create: To create a client.

    list: Lists all the clients.

    retrieve: To get a client data.

    update: To update all client data fields.

    partial_update: To update one or more client data fields.

    destroy: To delete a client.
    """
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
    ViewSet to perform CRUD operation on the Project model.

    create: To create a project.

    list: Lists all the projects.

    retrieve: To get a project data.

    update: To update all project data fields.

    partial_update: To update one or more project data fields.

    destroy: To delete a project.
    """
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer
