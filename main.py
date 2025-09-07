from libro import Libro
from usuario import Usuario
from biblioteca import Biblioteca

def menu():
    print("\n=== Sistema de Biblioteca Digital ===")
    print("1. Agregar libro")
    print("2. Eliminar libro")
    print("3. Registrar usuario")
    print("4. Eliminar usuario")
    print("5. Prestar libro")
    print("6. Devolver libro")
    print("7. Buscar libro")
    print("8. Listar préstamos de un usuario")
    print("9. Salir")

if _name_ == "_main_":
    biblioteca = Biblioteca()

    while True:
        menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")
            biblioteca.agregar_libro(Libro(titulo, autor, categoria, isbn))

        elif opcion == "2":
            isbn = input("Ingrese ISBN del libro a eliminar: ")
            biblioteca.eliminar_libro(isbn)

        elif opcion == "3":
            nombre = input("Nombre del usuario: ")
            user_id = input("ID de usuario: ")
            biblioteca.registrar_usuario(Usuario(nombre, user_id))

        elif opcion == "4":
            user_id = input("Ingrese ID de usuario a eliminar: ")
            biblioteca.eliminar_usuario(user_id)

        elif opcion == "5":
            user_id = input("ID de usuario: ")
            isbn = input("ISBN del libro: ")
            biblioteca.prestar_libro(user_id, isbn)

        elif opcion == "6":
            user_id = input("ID de usuario: ")
            isbn = input("ISBN del libro: ")
            biblioteca.devolver_libro(user_id, isbn)

        elif opcion == "7":
            campo = input("Buscar por (titulo/autor/categoria/isbn): ").strip().lower()
            valor = input(f"Ingrese {campo}: ")
            resultados = biblioteca.buscar_libro(**{campo: valor})
            if resultados:
                print("Resultados:")
                for r in resultados:
                    print(" -", r)
            else:
                print("No se encontraron coincidencias.")

        elif opcion == "8":
            user_id = input("ID de usuario: ")
            prestamos = biblioteca.listar_prestamos(user_id)
            if prestamos:
                print("Libros prestados:")
                for l in prestamos:
                    print(" -", l)
            else:
                print("El usuario no tiene libros prestados.")

        elif opcion == "9":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida.")
