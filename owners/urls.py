from django.urls import path
from django.urls.resolvers import URLPattern

from owners.views import OwnersView, DogsView

urlpatterns = [
    path('',OwnersView.as_view()),
    path('/dogs',DogsView.as_view()),
]