from django.urls import path

from app.views import home, up

urlpatterns = [
    path('', home),
    path('up/<int:id>/', up),
]
