from classDepartamento import Departamento

class Area(Departamento):  # Departamento de marketing
    def __init__(self):
        super().__init__()
        self._investigacion_mercado = ()
        self._creacion_marca = ()
        self._estrategia_publicidad = ()

    # Getters y Setters
    def get_investigacion_mercado(self):
        return self._investigacion_mercado

    def set_investigacion_mercado(self, investigacion_mercado):
        self._investigacion_mercado = investigacion_mercado

    def get_creacion_marca(self):
        return self._creacion_marca

    def set_creacion_marca(self, creacion_marca):
        self._creacion_marca = creacion_marca

    def get_estrategia_publicidad(self):
        return self._estrategia_publicidad

    def set_estrategia_publicidad(self, estrategia_publicidad):
        self._estrategia_publicidad = estrategia_publicidad

    def mostrar_informacion(self):
        info = super().mostrar_informacion()
        return (f": {info}, Area de: {self._investigacion_mercado}, Area de: {self._creacion_marca},"
                f" Area de: {self._estrategia_publicidad})")