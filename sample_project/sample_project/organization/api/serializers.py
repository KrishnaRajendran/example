from rest_framework import serializers
from sample_project.organization import models as organization_models


class TeamSerializers(serializers.ModelSerializer):
    """
    Serializer for the Team model.
    """

    class Meta:
        model = organization_models.Team
        fields = "__all__"


class DepartmentSerializers(serializers.ModelSerializer):
    """
    Serializer for the Department model.
    """

    class Meta:
        model = organization_models.Department
        fields = "__all__"


class DesignationSerializers(serializers.ModelSerializer):
    """
    Serializer for the Designation model.
    """

    class Meta:
        model = organization_models.Designation
        fields = "__all__"
