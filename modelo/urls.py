from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('proyecto/proyecto',views.listar_proyectos,name='lista_proyectos'),
    path('proyecto/proyecto/<int:id_proyecto>/',views.tarea_proyecto,name='tarea_proyecto'),
    path('tarea/tarea/<int:id_tarea>/',views.usuario_tarea,name='usuario_tarea'),
    #tareas con texto x en observacion durante la asignacion
    path('tarea/tarea/<str:texto_observacion>/',views.texto_tarea_asignacion,name='observacion_asignacion')
]
