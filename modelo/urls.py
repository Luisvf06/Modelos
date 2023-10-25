from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('proyecto/proyecto',views.listar_proyectos,name='lista_proyectos'),
    path('proyecto/proyecto/<int:id_proyecto>/',views.tarea_proyecto,name='tarea_proyecto'),
    path('tarea/tarea/<int:id_tarea>/',views.usuario_tarea,name='usuario_tarea'),
    path('tarea/tarea/<str:texto_observacion>/',views.texto_tarea_asignacion,name='observacion_asignacion'),
    #Crear una URL que muestre todos los proyectos que se han creado entre dos fechas y el estado sea “Completada”.
    #path('proyecto/proyecto/<int:anho_init>/<int:mes_init>/<int:dia_init>/<int:anho_fin>/<int:mes_fin>/<int:dia_fin>/',views.proyectos_rango,#name='proyectos_rango') no funciona

    #Crear una URL que muestre todos las tareas que se han creado entre dos años y el estado sea “Completada”
    path('proyecto/proyecto/<int:anho_init>/<int:anho_fin>/',views.tareas_anhos,name='tareas_2anhos')
]
