# Ejercicio 3 - Consulta de alumnos con criterios combinados

alumnos = [
    {"nombre": "Lautaro", "curso": "3°3°", "promedio": 8.5, "trabajos": 7},
    {"nombre": "Santiago", "curso": "3°3°", "promedio": 7.2, "trabajos": 6},
    {"nombre": "Bautista", "curso": "3°3°", "promedio": 9.1, "trabajos": 8},
    {"nombre": "Valentino", "curso": "3°3°", "promedio": 6.5, "trabajos": 5},
    {"nombre": "Mateo", "curso": "3°3°", "promedio": 8.8, "trabajos": 9},
    {"nombre": "Tomás", "curso": "3°3°", "promedio": 5.9, "trabajos": 4},
    {"nombre": "Franco", "curso": "3°3°", "promedio": 9.5, "trabajos": 10},
    {"nombre": "Agustín", "curso": "3°3°", "promedio": 7.8, "trabajos": 7},
    {"nombre": "Nicolás", "curso": "3°3°", "promedio": 6.8, "trabajos": 6},
    {"nombre": "Lucas", "curso": "3°3°", "promedio": 8.2, "trabajos": 8}
]

promedio_minimo = float(input("Ingrese el promedio mínimo requerido: "))
trabajos_minimos = int(input("Ingrese la cantidad mínima de trabajos entregados: "))

cantidad_cumplen = 0
cantidad_no_cumplen = 0

mejor_alumno = None
mejor_promedio = 0

print("\nAlumnos que cumplen ambos criterios:")

for alumno in alumnos:

    if alumno["promedio"] >= promedio_minimo and alumno["trabajos"] >= trabajos_minimos:

        print(f"Nombre: {alumno['nombre']}")
        print(f"Curso: {alumno['curso']}")
        print(f"Promedio: {alumno['promedio']}")
        print(f"Trabajos entregados: {alumno['trabajos']}")
        print("-" * 30)

        cantidad_cumplen += 1

        # Comparación manual para encontrar el promedio más alto
        if mejor_alumno is None or alumno["promedio"] > mejor_promedio:
            mejor_alumno = alumno
            mejor_promedio = alumno["promedio"]

    else:
        cantidad_no_cumplen += 1

print(f"\nCantidad de alumnos que cumplen: {cantidad_cumplen}")
print(f"Cantidad de alumnos que no cumplen: {cantidad_no_cumplen}")

if mejor_alumno is not None:
    print("\nAlumno con el promedio más alto entre los que cumplen:")
    print(f"Nombre: {mejor_alumno['nombre']}")
    print(f"Promedio: {mejor_alumno['promedio']}")
else:
    print("Ningún alumno cumple con las condiciones.")