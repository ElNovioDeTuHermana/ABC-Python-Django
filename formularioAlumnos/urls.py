
from django.urls import path
from . import views

urlpatterns = [
    path('', views.alumno_list_view, name='alumno_list'),
    path('new', views.alumno_create_view, name='alumno_create'),
    path('<int:id>/edit', views.alumno_update_view, name='alumno_update'),
    path('<int:id>/delete', views.alumno_delete_view, name='alumno_delete'),
    path('estadisticas/', views.estadisticas_alumnos_view, name='estadisticas_alumnos'),
]
