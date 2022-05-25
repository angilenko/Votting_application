from django.contrib import admin
from django.urls import path
from poll_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('api/v1/poll', PollAPIView.as_view()),
    path('api/v1/poll/<int:pk>', PollAPIViewDetail.as_view()),
    path('api/v1/poll/active', PollActiveAPIView.as_view()),
    path('api/v1/poll/finished', PollFinishedAPIView.as_view()),
    path('api/v1/add_vote', add_vote),
    path('api/v1/poll/winner/<int:pk>', get_winner),
    path('api/v1/poll/members/<int:pk>', get_members),
]
