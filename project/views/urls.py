from django.urls import path, include

urlpatterns = [
    path('v1/', include('views.v1.urls.py')),
]
