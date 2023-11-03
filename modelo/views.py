from django.shortcuts import render
from .models import Proyecto
from .models import Tarea
from .models import Usuario
from .models import Comentario
from .models import Asignacion_de_tarea
from .models import Etiqueta
from django.db.models import Q
from django.views.defaults import page_not_found
from django.views.defaults import bad_request
from django.views.defaults import server_error
from django.views.defaults import permission_denied

# Create your views here.
def index(request):
    return render(request,'index.html')

def listar_proyectos(request):
    proyecto=Proyecto.objects.prefetch_related('colaboradores').select_related('creador')
    return render(request,'proyecto/lista.html',{'proyecto_mostrar':proyecto})

def tarea_proyecto(request,id_proyecto):
    tareas=Tarea.objects.select_related('proyecto')
    tareas=tareas.filter(proyecto=id_proyecto).order_by("-Fecha_de_Creación")
    return render(request, 'proyecto/lista.html',{'tarea_proyect':tareas})

def usuario_tarea(request,id_tarea):
    usuarios=Asignacion_de_tarea.objects.select_related('usuario')
    usuarios=usuarios.filter(tarea=id_tarea).order_by('Fecha_de_Asignación')
    return render(request,'tarea/listatarea.html',{'usuario_tarea':usuarios})

def texto_tarea_asignacion(request, texto_observacion):
    tareas=Asignacion_de_tarea.objects.select_related('tarea')
    tareas=tareas.filter(Observaciones__contains=texto_observacion)
    return render(request,'tarea/listatarea.html',{'observacion_tarea':tareas})

def tareas_anhos(request,anho_init,anho_fin):
    tareas=Tarea.objects.select_related('proyecto')
    tareas=tareas.filter(Q(Fecha_de_Creación__year__gte=anho_init) & Q(Fecha_de_Creación__year__lte=anho_fin) & Q(Estadio='Co'))
    #tareas=tareas.filter((Fecha_de_Creación__year__gte=anho_init).filter(Fecha_de_Creación__year__lte=anho_fin).filter(Estadio='Co'))
    return render(request,'tarea/listatarea.html',{'tareas_anhos':tareas})

def ultimo_comentario(request,id_proyecto):
    comentarios=Comentario.objects.select_related('tarea').prefetch_related('autor')
    comentario=comentarios.filter(tarea__proyecto=id_proyecto).order_by('-Fecha_de_Comentario')[:1].get()
    return render(request,'comentario/listacomentario.html',{'comentario':comentario})

def comentario_palabra_anho(request,palabra,anho):
    comentarios=Comentario.objects.select_related('tarea').prefetch_related('autor')
    comentarios=comentarios.filter(Contenido__startswith=palabra).filter(Fecha_de_Comentario__year=anho)
    return render(request,'comentario/listacomentario.html',{'comentarios_palabra':comentarios})

def etiquetas_proyecto(request, id_proyecto):
    etiquetas=Etiqueta.objects.prefetch_related('tarea')
    etiquetas=etiquetas.filter(tarea__proyecto=id_proyecto)
    return render(request,'etiqueta/listaetiqueta.html',{'etiquetas_proyecto':etiquetas})

def usuarios_sin_tarea(request):
    usuarios=Usuario.objects.exclude(asignacion_de_tarea__isnull=False)#excluyo los valores no nulos de asignacion_de_tarea
    return render(request, 'usuario/listausuario.html',{'usuarios_sin_tarea':usuarios})

def mi_error_400(request,exception=None):
    return render(request,'errores/400.html',None,None,400)#solicitud incorrecta

def mi_error_403(request,exception=None):
    return render(request,'errores/403.html',None,None,403)#permiso denegado

def mi_error_404(request,exception=None):
    return render(request,'errores/404.html',None,None,404)#not found

def mi_error_500(request,exception=None):
    return render(request,'errores/500.html',None,None,500)#error del servidor


#He intentado hacer el ejercicio 6 con el enunciado original pero no lo he conseguido
#def proyecto_fechas(request,anho_init=2000,mes_init=1,dia_init=1,anho_fin=2023,mes_fin=12,dia_fin=31):
#    tareas=Tarea.objects.prefetch_related('usuario').select_related('proyecto')
#    tareas=tareas.filter(Q(proyecto__Fecha_de_Inicio__year__gte=anho_init)|Q(proyecto__Fecha_de_Inicio__year=(anho_init) & Q (proyecto__Fecha_de_Inicio__month__gte=mes_init))|Q(proyecto__Fecha_de_Inicio__year=(anho_init) & Q(proyecto__Fecha_de_Inicio__month=mes_init)& Q(proyecto__Fecha_de_Inicio__day__gte=dia_init)) & Q(proyecto__Fecha_de_Inicio__year__lte=anho_fin)|Q(proyecto__Fecha_de_Inicio__year=(anho_fin) & Q(proyecto__Fecha_de_Inicio__month__lte=mes_fin))|Q(proyecto__Fecha_de_Inicio__year=(anho_fin) & Q(proyecto__Fecha_de_Inicio__month=mes_fin)& Q(proyecto__Fecha_de_Inicio__day__lte=dia_fin)) &(Q(Estadio='Co')))
#    return render(request,'proyecto/proyecto.html',{'proyectos_fecha':tareas})
