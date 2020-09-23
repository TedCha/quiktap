from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='posts-front-page'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path(
        'post/<int:pk>/edit/',
        views.PostUpdateView.as_view(),
        name='post-update'
    ),
    path(
        'post/<int:pk>/delete/',
        views.PostDeleteView.as_view(),
        name='post-delete'
    ),
    path(
        'user/<str:username>/',
        views.UserPostListView.as_view(),
        name='user-posts'
    ),
    path(
        'post/<int:pk>/comment/new/',
        views.CommentCreateView.as_view(),
        name='comment-create'
    ),
    path(
        'post/comment/<int:pk>/update/',
        views.CommentUpdateView.as_view(),
        name='comment-update'
    ),
    path(
        'post/comment/<int:pk>/delete/',
        views.CommentDeleteView.as_view(),
        name='comment-delete'
    ),
]
