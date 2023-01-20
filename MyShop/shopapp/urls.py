from django.urls import path
from . import views
urlpatterns = [
    # path("home/", views.home.as_view(), name="home"),
    path("pr/", views.Products, name="product"),
    path("pr/<int:id>/", views.myprod, name="pr"),
]
