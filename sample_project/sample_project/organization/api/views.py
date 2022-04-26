from rest_framework import viewsets
from sample_project.organization import models
from . import serializers


class TeamViewSet(viewsets.ModelViewSet):
    """
    ViewSet to perform CRUD operation on the Team model.

    create: To create a team.

    list: Lists all the teams.

    retrieve: To get a team data.

    update: To update all team data fields.

    partial_update: To update one or more team data fields.

    destroy: To delete a team.
    """

    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamSerializers


class DepartmentViewSet(viewsets.ModelViewSet):
    """
    ViewSet to perform CRUD operation on the Department model.

    create: To create a department.

    list: Lists all the departments.

    retrieve: To get a department data.

    update: To update all department data fields.

    partial_update: To update one or more department data fields.

    destroy: To delete a department.
    """

    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializers


class DesignationViewSet(viewsets.ModelViewSet):
    """
    ViewSet to perform CRUD operation on the Designation model.

    create: To create a designation.

    list: Lists all the designations.

    retrieve: To get a designation data.

    update: To update all designation data fields.

    partial_update: To update one or more designation data fields.

    destroy: To delete a designation.
    """

    queryset = models.Designation.objects.all()
    serializer_class = serializers.DesignationSerializers
