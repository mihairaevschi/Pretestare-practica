from django.urls import path
from .views import (
    SendFeedbackView
)

urlpatterns = [
    path('create-feedback/', SendFeedbackView.as_view()),
]
