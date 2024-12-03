from django.urls import path, include

urlpatterns = [
    path('', include('views.v1.urls_repo.hellow_world.py')),
]
