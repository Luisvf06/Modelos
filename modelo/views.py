from django.shortcuts import render
from .models import Proyecto
from .models import Tarea
from .models import Usuario
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
    usuario=Usuario.objects.select_related('usuario')#cambiar