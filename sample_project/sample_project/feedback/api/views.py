from rest_framework.decorators import APIView
from sample_project.feedback import models
from rest_framework.response import Response
from . import serializers

class FeedbackView(APIView):
    def get(self, request):
        feedback = models.Feedback.objects.all()
        serializer = serializers.FeedbackSerializer(feedback, many=True)
        return Response(serializer.data)
