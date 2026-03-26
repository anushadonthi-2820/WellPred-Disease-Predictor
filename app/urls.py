from django.urls import path
from app import views

urlpatterns = [
    path("", views.render_home, name="home"),
    path("heart", views.render_heart, name="heart"),
    path("kidney", views.render_kidney, name="kidney"),
    path("cervical", views.render_cervical, name="cervical"),
]