from classEmpleado import Empleado
from classArea import Area

class Director(Empleado,Area):
    def __init__(self):
        super().__init__()
        self._region= ""

    # Getters y Setters
    def get_region(self):
        return self._region

    def set_region(self, region):
        self._region = region

    def mostrar_informacion(self):
        info = super().mostrar_informacion()
        return f"{info}La region del director es {self._region}"

