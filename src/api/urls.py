from django.urls import (include, path, )

urlpatterns = [
    path('1.0.0/', include(('api.v1_0_0.router', 'api'), namespace='1.0.0')),
]
