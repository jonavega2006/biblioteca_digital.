class Libro:
    def _init_(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn
        # Tupla inmutable que combina autor y título
        self.clave = (autor, titulo)

    def _repr_(self):
        return f"{self.titulo} - {self.autor} ({self.categoria}, ISBN: {self.isbn})"
