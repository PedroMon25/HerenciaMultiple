from classEmpleado import Empleado
from classDepartamento import Departamento

class Gerente(Empleado,Departamento):
    def __init__(self):
        super().__init__()
        self._sucursal= ""

    # Getters y Setters
    def get_sucursal(self):
        return self._sucursal

    def set_sucursal(self, sucursal):
        self._sucursal = sucursal

    def mostrar_informacion(self):
        info = super().mostrar_informacion()
        return f"{info} La sucursal a cargo es: {self._sucursal}"

