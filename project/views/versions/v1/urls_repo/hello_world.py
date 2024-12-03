from django.urls import path

from ..apis import hello_world

app_name = 'auth'
urlpatterns = [
    path('helloworld/', hello_world, name='helloWorld'),
]
