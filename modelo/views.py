from django.shortcuts import render
from .models import Proyecto
from .models import Tarea
from .models import Usuario
from .models import Comentario
from .models import Asignacion_de_tarea
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request,'index.html')

def listar_proyectos(request):
    proyecto=Proyecto.objects.prefetch_related('colaboradores').select_related('creador')
    return render(request,'proyecto/proyecto.html',{'proyecto_mostrar':proyecto})

def tarea_proyecto(request,id_proyecto):
    tareas=Tarea.objects.select_related('proyecto')
    tareas=tareas.filter(proyecto=id_proyecto).order_by("-Fecha_de_Creación")
    return render(request, 'proyecto/proyecto.html',{'tarea_proyect':tareas})

def usuario_tarea(request,id_tarea):
    usuarios=Asignacion_de_tarea.objects.select_related('usuario')
    usuarios=usuarios.filter(tarea=id_tarea).order_by('Fecha_de_Asignación')
    return render(request,'tarea/tarea.html',{'usuario_tarea':usuarios})

def texto_tarea_asignacion(request, texto_observacion):
    tareas=Asignacion_de_tarea.objects.select_related('tarea')
    tareas=tareas.filter(Observaciones__contains=texto_observacion)
    return render(request,'tarea/tarea.html',{'observacion_tarea':tareas})

#def proyectos_rango(request,anho_init,mes_init_dia_init,anho_fin,mes_fin,dia_fin):
#    proyecto=Proyecto.objects.prefetch_related('colaboradores').select_related('creador')
#    proyecto=proyecto.filter(Q(Fecha_de_Inicio__year<=anho_init)|Q(Fecha_de_Inicio__year=anho_init & Fecha_de_Inicio__month<mes_init)|Q#(Fecha_de_Inicio__year=anho_init & Fecha_de_Inicio__month=mes_init)) no soy capaz de hacer funcionar los or 

def tareas_anhos(request,anho_init,anho_fin):
    tareas=Tarea.objects.select_related('proyecto')
    tareas=tareas.filter(Q(Fecha_de_Creación__year__gte=anho_init) & Q(Fecha_de_Creación__year__lte=anho_fin) & Q(Estadio='Co'))
    #tareas=tareas.filter((Fecha_de_Creación__year__gte=anho_init).filter(Fecha_de_Creación__year__lte=anho_fin).filter(Estadio='Co'))
    return render(request,'tarea/tarea.html',{'tareas_anhos':tareas})

def ultimo_comentario(request,id_proyecto):
    comentarios=Comentario.objects.select_related('tarea').prefetch_related('autor')
    comentario=comentarios.filter(tarea__proyecto=id_proyecto).order_by('-Fecha_de_Comentario')[:1].get()
    return render(request,'comentario/comentario.html',{'comentario':comentario})