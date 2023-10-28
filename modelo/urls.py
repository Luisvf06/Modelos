from django.urls import path
from .import views

urlpatterns = [
    #Desde una página de Inicio debe poder acceder a todas las URLs que se indiquen. Esto no significa que no pueda acceder a algunas URLs desde otros sitios. Pero desde la página de Inicio tengo que poder acceder a un ejemplo de las URLs que se realicen a continuación.
    path('',views.index,name='index'),

    #Crea una URL que muestre una lista de todos los proyectos de la aplicación con sus datos correspondientes.
    path('proyecto/proyecto',views.listar_proyectos,name='lista_proyectos'),

    #Crear una URL que muestre todas las tareas que están asociadas a un proyecto, ordenadas por fecha de creación descendente.
    path('proyecto/proyecto/<int:id_proyecto>/',views.tarea_proyecto,name='tarea_proyecto'),

    #Crear una URL que muestre todos los usuarios que están asignados a una tarea ordenados por la fecha de asignación de la tarea de forma ascendente. 
    path('tarea/tarea/<int:id_tarea>/',views.usuario_tarea,name='usuario_tarea'),

    #Crear una URL que muestre todas las tareas que tengan un texto en concreto en las observaciones a la hora de asignarlas a un usuario.
    path('tarea/tarea/<str:texto_observacion>/',views.texto_tarea_asignacion,name='observacion_asignacion'),



    #Crear una URL que muestre todos los tareas que se han creado entre dos años y el estado sea “Completada”.
    path('tarea/tarea/<int:anho_init>/<int:anho_fin>/',views.tareas_anhos,name='tareas_anhos'),

    #Crear una URL que obtenga el último usuario que ha comentado en una tarea de un proyecto en concreto.
    path('comentario/comentario/<int:id_proyecto>/',views.ultimo_comentario,name='ultimo_comentario'),

    #Crear una URL que obtenga todos los comentarios de una tarea que empiecen por la palabra que se pase en la URL y que el año del comentario sea uno en concreto.
    path('comentario/comentario/<str:palabra>/<int:anho>',views.comentario_palabra_anho,name='comentarios_palabra_fecha'),

    #Crear una URL que obtenga todas las etiquetas que se han usado en todas las tareas de un proyecto.
    path('etiqueta/etiqueta/<int:id_proyecto>/',views.etiquetas_proyecto,name='etiquetas_proyecto'),

    #Crear una URL que muestre todos los usuarios que no están asignados a una tarea.
    path('usuario/usuario/',views.usuarios_sin_tarea,name='usuarios_sin_tarea'),

    #Crear una URL que muestre todos los proyectos que se han creado entre dos fechas y el estado sea “Completada”.
    #path('proyecto/proyecto/<int:anho_init>/<int:mes_init>/<int:dia_init>/<int:anho_fin>/<int:mes_fin>/<int:dia_fin>/',views.proyecto_fechas,name='proyecto_fechas_co')No funciona
]
