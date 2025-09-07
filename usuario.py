class Usuario:
    def _init_(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []

    def _repr_(self):
        return f"Usuario: {self.nombre} (ID: {self.user_id})"
