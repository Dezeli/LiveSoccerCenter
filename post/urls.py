from django.urls import path
from . import views

app_name = "post"
urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
    path("detail/<int:post_id>/", views.detail, name="detail"),
    path("edit/<int:post_id>/", views.edit, name="edit"),
    path("comment/<int:post_id>/", views.comment, name="comment"),
    path("barcelona", views.barca, name="barca"),
    path("ulsan", views.ulsan, name="ulsan"),
    path("test", views.test, name="test"),
]
