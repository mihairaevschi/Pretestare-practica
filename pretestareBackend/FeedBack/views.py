from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from .models import Feedback

from .serializers import (
    FeedbackSerializer
)

class SendFeedbackView(generics.ListCreateAPIView):
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
