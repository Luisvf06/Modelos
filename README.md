Dudas:
En el ejercicio 6, en el que hay que filtrar las tareas creadas entre dos años, hay que usar gte y lte para el mayor o igual/menor o igual, pero intentando hacer el ejercicio original, que era por proyectos en lugar de tareas y con fecha (año,mes y dia) en lugar de años, intenté hacer igualdades con __exact, como vi en stackoverflow, pero daba error, solo podía usar =

En la diapositiva 49 del tema 4, pone handler404=.... pero tuve problemas haciendo los errores y al consultar el ejemplo que hicimos en clase de biblioteca, tengo handler400=handler=.... He probado ambos y funcionan igual, pero no sé si hay alguna diferencia.

If: comentario/listacomentario.html
    etiqueta/etiquetaproy.html
    proyecto/lista.html
    tarea/listatarea.html

Empty: comentario/listacomentario.html
        tarea/listatarea.html
        usuario/listausuario.html

Filter:
    proyecto/lista.html
        |date:"Y"
        |upper
        |wordcount
    tarea/listatarea.html
        |divisibleby:
        |get_digit:
        |length
    etiqueta/listaetiqueta.html
        |title