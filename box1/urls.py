from.import views
from django.urls import include, path

urlpatterns = [
    path("", views.index, name="index"),
    path('api-auth/', include('rest_framework.urls')),
]
