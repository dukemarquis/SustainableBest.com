from django.urls import path

from . import views

app_name = "main"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("recommend/", views.recommend, name="recommend"),
    path("pid_<int:pk>/recommend_result/", views.RecommendResultView.as_view(), name="recommend_result"),
    path("pid_<int:pk>/", views.SusProductDetailView.as_view(), name="detail"),
]