from django.shortcuts import render
from .models import Proyecto
from .models import Tarea
from .models import Usuario
from .models import Asignacion_de_tarea
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
    #tareas=tareas.filter(Fecha_de_Creación__year<anho_init)