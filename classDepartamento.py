class Departamento: #Departamento de marketing
    def __init__(self):
        self._nombre_departamento = ""
        self._objetivos = ""
        self._recursos = ""

    # Getters y Setters
    def get_nombre_departamento(self):
        return self._nombre_departamento

    def set_nombre_departamento(self, nombre_departamento):
        self._nombre_departamento = nombre_departamento

    def get_objetivos(self):
        return self._objetivos

    def set_objetivos(self, objetivos):
        self._objetivos = objetivos

    def get_recursos(self):
        return self._recursos

    def set_recursos(self, recursos):
        self._recursos = recursos

    def mostrar_informacion(self):
        return (f"Nombre del departamento: {self._nombre_departamento}, Objetivos: {self._objetivos},"
                f" Recursos necesarios: {self._recursos}")
