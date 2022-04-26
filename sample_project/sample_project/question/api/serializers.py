from rest_framework import serializers
from sample_project.question import models as question_models


class CoreValueSerializer(serializers.ModelSerializer):
    """
    Serializer for the CoreValue model.
    """

    class Meta:
        model = question_models.CoreValue
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    """
    Serializer for the Question model.
    """
    type = serializers.SerializerMethodField()
    option_group = serializers.StringRelatedField()
    core_value = serializers.StringRelatedField()

    def get_type(self, obj):
        return obj.get_type_display()

    class Meta:
        model = question_models.Question
        fields = "__all__"


class AnswerSerializer(serializers.ModelSerializer):
    """
    Serializer for the Answer model.
    """

    class Meta:
        model = question_models.Answer
        fields = "__all__"
