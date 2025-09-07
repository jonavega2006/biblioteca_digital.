from libro import Libro
from usuario import Usuario

class Biblioteca:
    def _init_(self):
        self.libros = {}        # {isbn: Libro}
        self.usuarios = {}      # {user_id: Usuario}
        self.prestamos = {}     # {user_id: [Libro, ...]}

    # --- Gestión de libros ---
    def agregar_libro(self, libro: Libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.titulo}' agregado.")
        else:
            print("El libro ya existe en la biblioteca.")

    def eliminar_libro(self, isbn: str):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado.")
        else:
            print("El libro no está registrado.")

    # --- Gestión de usuarios ---
    def registrar_usuario(self, usuario: Usuario):
        if usuario.user_id not in self.usuarios:
            self.usuarios[usuario.user_id] = usuario
            self.prestamos[usuario.user_id] = []
            print(f"Usuario '{usuario.nombre}' registrado.")
        else:
            print("El usuario ya existe.")

    def eliminar_usuario(self, user_id: str):
        if user_id in self.usuarios:
            del self.usuarios[user_id]
            del self.prestamos[user_id]
            print("Usuario eliminado.")
        else:
            print("Usuario no encontrado.")

    # --- Préstamos ---
    def prestar_libro(self, user_id: str, isbn: str):
        if user_id in self.usuarios and isbn in self.libros:
            libro = self.libros[isbn]
            if libro not in self.prestamos[user_id]:
                self.prestamos[user_id].append(libro)
                self.usuarios[user_id].libros_prestados.append(libro)
                print(f"Libro '{libro.titulo}' prestado a {self.usuarios[user_id].nombre}.")
            else:
                print("Este libro ya está prestado a este usuario.")
        else:
            print("Usuario o libro no encontrado.")

    def devolver_libro(self, user_id: str, isbn: str):
        if user_id in self.usuarios and isbn in self.libros:
            libro = self.libros[isbn]
            if libro in self.prestamos[user_id]:
                self.prestamos[user_id].remove(libro)
                self.usuarios[user_id].libros_prestados.remove(libro)
                print(f"Libro '{libro.titulo}' devuelto por {self.usuarios[user_id].nombre}.")
            else:
                print("El usuario no tiene prestado este libro.")
        else:
            print("Usuario o libro no encontrado.")

    # --- Búsquedas ---
    def buscar_libro(self, **kwargs):
        resultados = []
        for libro in self.libros.values():
            if all(getattr(libro, k) == v for k, v in kwargs.items()):
                resultados.append(libro)
        return resultados

    def listar_prestamos(self, user_id: str):
        return self.prestamos.get(user_id, [])
