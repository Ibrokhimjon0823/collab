from django.urls import path
from core import views

urlpatterns = [
    path('generics/', views.PostList.as_view()),
    path('generics/<int:pk>/', views.PostDetail.as_view()),

    path('apiview/', views.ListCreateAPIView.as_view()),
    path('apiview/<int:pk>/', views.ReadUpdateDeleteAPIView.as_view()),

    path('func/', views.post_list_create),
    path('func/<int:pk>/', views.post_read_update_delete),
]
