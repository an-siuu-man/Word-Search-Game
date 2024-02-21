from django.urls import path

from . import views
urlpatterns = [
    path("", views.homepage, name = "homepage"),
    path("game", views.rendering_the_game, name = "gamepage")
    ]