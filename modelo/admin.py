from django.contrib import admin
from .models import Usuario
from .models import Tarea
from .models import Proyecto
from .models import Etiqueta
from .models import Asignacion_de_tarea
from .models import Comentario

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Tarea)
admin.site.register(Proyecto)
admin.site.register(Etiqueta)
admin.site.register(Asignacion_de_tarea)
admin.site.register(Comentario)