# Script de Asignación de Correctores para trabajos grupales

Para ejecutar el script: 
```
	python3 asignacion.py <individuales> <cantidades>
```
Donde: 
* `individuales` es la ruta a un archivo tsv (para que sea simplemente copiar la planilla y listo) con el formato: 
```
	Ayudante_individual 	NumGrupo (copiar columnas de la planilla)
```
* `cantidades` es un tsv (solo por consitencia con el anterior) con el formato: 
```
	Ayudante 	cant_grupos_a_corregir
```

Lo que hace el script es cargar en un diccionario la relación "Ayudante individual-Grupo", para luego no dejar que alquien que haya corregido ya a los integrantes de algún grupo, les pueda volver a corregir. 
Luego, carga las cantidades de grupos a corregir por cada corrector. Se asume que la cantidad de grupos a asignar corresponde con la suma de la disponibilidad de los correctores. También, que los Números de grupos van de 1 a N, sin saltos ni nada por el estilo (sino, no va a andar). Se crea una lista con los correctores, donde cada corrector aparece tantas veces como su disponibilidad diga.  

Para la asignación: se hace un shuffle de los correctores. Luego, se calculan los conflictos (corrector que corrija a un grupo con integrantes que ya corrigió en tps individuales). Agarra los ayudantes en conflicto y asigna al azar los grupos en conflicto entre esos ayudantes.

Problemas: 
- En caso que todos los grupos en conflicto sean del mismo ayudante, entonces simplemente se vuelve a asignar de forma aleatoria. 
- En caso que el problema no tenga solución, el script se quedará loopeando para siempre.
- En caso que los conflictos que queden sean entre dos ayudantes pero en el que ambos quedaron banneados de corregir a esos grupos, el programa quedará loopeado para siempre (known issue).