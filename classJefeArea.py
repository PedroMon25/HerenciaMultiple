from classEmpleado import Empleado
from classArea import Area

class JefeArea(Empleado,Area):
    def __init__(self):
        super().__init__()
        self._reporte_estadistico = ""
        self._reporte_incidentes = ""

    # Getters y Setters
    def get_reporte_estadistico(self):
        return self._reporte_estadistico

    def set_reporte_estadistico(self, reporte_estadistico):
        self._reporte_estadistico = reporte_estadistico

    def get_reporte_incidentes(self):
        return self._reporte_incidentes

    def set_reporte_incidentes(self, reporte_incidentes):
        self._reporte_incidentes = reporte_incidentes

    def mostrar_informacion(self):
        info = super().mostrar_informacion()
        return f"{info} Estadisticas: {self._reporte_estadistico}, Incidentes: {self._reporte_incidentes}"
