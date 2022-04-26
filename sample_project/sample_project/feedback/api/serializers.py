from rest_framework import serializers
from sample_project.feedback import models as feedback_models
from sample_project.project.api import serializers as project_serializers
from sample_project.question.api import serializers as question_serializers


class FeedbackSectionSerializer(serializers.ModelSerializer):
    """
    Serializer for the Feedback Section model.
    """
    type = serializers.SerializerMethodField()
    questions = question_serializers.QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = feedback_models.FeedbackSection
        fields = "__all__"

    def get_type(self, obj):
        return obj.get_type_display()


class FeedbackSerializer(serializers.ModelSerializer):
    """
    Serializer for the Feedback model.
    """
    sections = FeedbackSectionSerializer(many=True, read_only=True)
    projects = project_serializers.ProjectSerializer(read_only=True)

    class Meta:
        model = feedback_models.Feedback
        fields = "__all__"


class TemplateSerializer(serializers.ModelSerializer):
    """
    Serializer for the Template Section model.
    """

    class Meta:
        model = feedback_models.Template
        fields = "__all__"
