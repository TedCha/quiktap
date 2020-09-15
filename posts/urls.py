from django.urls import path

from . import views

urlpatterns = [
    path('', views.FrontPageView.as_view(), name='posts-front-page'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='posts-detail'),
]
