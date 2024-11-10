from classPersona import Persona

class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self._puesto = ""
        self._sueldo = 0
        self._nomina = ""

    # Getters y Setters
    def get_puesto(self):
        return self._puesto

    def set_puesto(self, puesto):
        self._puesto = puesto

    def get_sueldo(self):
        return self._sueldo

    def set_sueldo(self, sueldo):
        self._sueldo = sueldo

    def get_nomina(self):
        return self._nomina

    def set_nomina(self, nomina):
        self._nomina = nomina

    def mostrar_informacion(self):
        info = super().mostrar_informacion()
        return f"{info}, Puesto: {self._puesto}, Sueldo:{self._sueldo}, NoNomina: {self._nomina}"
