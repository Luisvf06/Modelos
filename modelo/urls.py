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
    path('tarea/tarea/<int:anho_init>/<int:anho_fin>/',views.tareas_anhos,name='tareas_anhos'),
    #Crear una URL que obtenga el último usuario que ha comentado en una tarea de un proyecto en concreto.
    path('comentario/comentario/<int:id_proyecto>/',views.ultimo_comentario,name='ultimo_comentario'),
    #Crear una URL que obtenga todos los comentarios de una tarea que empiecen por la palabra que se pase en la URL y que el año del comentario sea uno en concreto.
    path('comentario/comentario/<str:palabra>/<int: anho>',views.comentario_palabra_anho,name='comentarios_palabra_fecha')
]
