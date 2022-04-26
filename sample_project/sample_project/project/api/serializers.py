from rest_framework import serializers
from sample_project.project import models as project_models


class ClientSerializer(serializers.ModelSerializer):
    """
    Serializer for the Client model.
    """

    class Meta:
        model = project_models.Client
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    """
    Serializer for the Project model.
    """
    client = serializers.StringRelatedField()
    project_manager = serializers.StringRelatedField()
    members = serializers.SerializerMethodField()

    def get_members(self, obj):
        member_list = []
        for member in obj.members.all():
            member_list.append(member.username)
        return member_list

    def validate(self, data):
        """
        Checks given project manager not exist in members field.
        """
        project_manager = data.get("project_manager")
        members = data.get("members")
        if project_manager in members:
            raise serializers.ValidationError(
                {'members': 'Please remove project manager from members'}
            )
        return data

    class Meta:
        model = project_models.Project
        fields = "__all__"
