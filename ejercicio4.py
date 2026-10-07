# Ejercicio 4 - Diagnóstico y reparación de un READ defectuoso

libros = [
    {"isbn": "978-001", "titulo": "El principito", "autor": "Antoine de Saint-Exupéry", "disponible": True},
    {"isbn": "978-002", "titulo": "1984", "autor": "George Orwell", "disponible": False},
    {"isbn": "978-003", "titulo": "Don Quijote", "autor": "Miguel de Cervantes", "disponible": True},
    {"isbn": "978-004", "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "disponible": True},
    {"isbn": "978-005", "titulo": "Fahrenheit 451", "autor": "Ray Bradbury", "disponible": False}
]

isbn_buscado = input("Ingrese el ISBN que desea buscar: ")

# -------------------------------------------------
# VERSIÓN INCORRECTA
# -------------------------------------------------

print("--- Versión incorrecta ---")

for libro in libros:
    if libro["isbn"] == isbn_buscado:
        print("Libro encontrado:")
        print(libro)
    else:
        print("Libro no encontrado")


# El problema es que el else pertenece a cada vuelta del for.
# Si el primer libro no coincide, muestra "Libro no encontrado"
# aunque todavía queden otros libros por revisar.
# Por eso el mensaje puede aparecer varias veces y ser incorrecto.
# El programa debe esperar a terminar la búsqueda antes de afirmar que no existe.


# -------------------------------------------------
# VERSIÓN CORREGIDA
# -------------------------------------------------

print("--- Versión corregida ---")

encontrado = False

for libro in libros:
    if libro["isbn"] == isbn_buscado:
        print("\nLibro encontrado:")
        print(f"ISBN: {libro['isbn']}")
        print(f"Título: {libro['titulo']}")
        print(f"Autor: {libro['autor']}")
        print(f"Disponible: {libro['disponible']}")

        encontrado = True
        break

if not encontrado:
    print("Libro no encontrado")