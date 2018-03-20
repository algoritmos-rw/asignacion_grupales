import random
import sys

# El archivo 'individuales' debe ser un tsv (para que sea simplemente copiar la planilla y listo) con el formato:
# Ayudante_individual num_grupo (copiar las columnas de la planilla)
# El archivo 'cantidades' simplemente es un tsv (solo para ser consistente con el anterior):
# Ayudante cant_grupos_a_corregir

SEPARADOR = '\t'
CORRUPTO = False

def calcular_conflictos(asignacion, banned):
    conflictos = []
    for i in range(len(asignacion)):
        if i in banned[asignacion[i]] and not CORRUPTO:
            conflictos.append(i)
    return conflictos

def todos_mismo_corrector(asignacion, conflictos):
    # Si todos son iguales al primero, son todos iguales
    return all(map(lambda c: asignacion[c] is asignacion[conflictos[0]], conflictos))

def asignar_random_ayudantes(ayudantes, banned):
    asignacion = ayudantes[:]
    random.shuffle(asignacion)

    conflictos = calcular_conflictos(asignacion, banned)
    while len(conflictos) > 0:
        # me fijo si los conflictos son todos del mismo, para no tener un loop infinito
        if todos_mismo_corrector(asignacion, conflictos):
            random.shuffle(asignacion)
            conflictos = calcular_conflictos(asignacion, banned)
            continue
        # agarro los ayudantes en conflicto:
        ayudantes = [asignacion[grupo] for grupo in conflictos]
        # desordeno
        random.shuffle(ayudantes)
        # asigno a los grupos
        for i in range(len(conflictos)):
            asignacion[conflictos[i]] = ayudantes[i]
        conflictos = calcular_conflictos(asignacion, banned)

    return asignacion


def main():
    banned = {}
    with open(sys.argv[1]) as individuales:
        for l in individuales:
            try:
                ay, grupo = l.rstrip().split(SEPARADOR)

                banned[ay] = banned.get(ay, [])
                # Los grupos se llaman G01, etc
                grupo = int(grupo[1:]) - 1
                banned[ay].append(grupo)
            except ValueError:
                #salteo alumnos sin grupo
                pass

    ayudantes = []
    with open(sys.argv[2]) as cantidades:
        for l in cantidades:
            ay, cantidad = l.rstrip().split(SEPARADOR)
            ayudantes += list([ay for i in range(int(cantidad))])

    asignacion = asignar_random_ayudantes(ayudantes, banned)

    for ay in asignacion:
        # imprimo dos veces para que quede ya para poner en la planilla
        # Ordenar la planilla por numero de grupo para copiar las asignaciones
        print(ay)
        print(ay)

main()


    


