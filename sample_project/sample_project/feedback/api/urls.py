from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.FeedbackView.as_view(), name="get")
]

