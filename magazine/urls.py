from django.urls import path

from . import views

urlpatterns = [
    path('', views.publications, name='publications'),
    path('<int:pk>', views.publication_detail, name='publication_detail'),
    path('<int:pk>/read', views.reader, name='reader'),
]