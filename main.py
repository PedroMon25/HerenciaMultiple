from classEmpleado import Empleado
from classArea import Area
from classDirector import Director
from classGerente import Gerente
from classJefeArea import JefeArea

def main():

    classEmpleado = Empleado()
    classEmpleado.set_nombre("Pedro")
    classEmpleado.set_apellido("Castro")
    classEmpleado.set_edad(20)
    classEmpleado.set_puesto("Supervisor")
    classEmpleado.set_sueldo(20000)
    classEmpleado.set_nomina(242001)

    classArea = Area()
    classArea.set_nombre_departamento("Recursos humanos")
    classArea.set_objetivos("Capacitacion")
    classArea.set_recursos("Empleados")
    classArea.set_investigacion_mercado("Competencia en el mercado")
    classArea.set_creacion_marca("Creacion de la marca en base a las necesidades del publico")
    classArea.set_estrategia_publicidad("Comparar competencia y solicitudes de los clientes")

    classDirector = Director()
    classDirector.set_nombre("Cesar")
    classDirector.set_apellido("Monroy")
    classDirector.set_edad(32)
    classDirector.set_puesto("Director general")
    classDirector.set_sueldo(200000)
    classDirector.set_nomina(242)
    classDirector.set_nombre_departamento("Recursos humanos")
    classDirector.set_objetivos("Capacitacion")
    classDirector.set_recursos("Empleados")
    classDirector.set_investigacion_mercado("Competencia en el mercado")
    classDirector.set_creacion_marca("Creacion de la marca en base a las necesidades del publico")
    classDirector.set_estrategia_publicidad("Comparar competencia y solicitudes de los clientes")
    classDirector.set_recursos("Sur")

    classGerente = Gerente()
    classGerente.set_nombre("Carlos")
    classGerente.set_apellido("Hernandez")
    classGerente.set_edad(30)
    classGerente.set_puesto("Gerente general")
    classGerente.set_sueldo(50000)
    classGerente.set_nomina(2001)
    classGerente.set_nombre_departamento("Recursos humanos")
    classGerente.set_objetivos("Capacitacion")
    classGerente.set_recursos("Empleados")
    classGerente.set_sucursal("Marketing CDMX")

    classJefeArea = JefeArea()
    classJefeArea.set_nombre("Eric")
    classJefeArea.set_apellido("Carrillo")
    classJefeArea.set_edad(22)
    classJefeArea.set_puesto("Jefe de area")
    classJefeArea.set_sueldo(15000)
    classJefeArea.set_nomina(34801)
    classJefeArea.set_nombre_departamento("Recursos humanos")
    classJefeArea.set_objetivos("Capacitacion")
    classJefeArea.set_recursos("Empleados")
    classJefeArea.set_investigacion_mercado("Competencia en el mercado")
    classJefeArea.set_creacion_marca("Creacion de la marca en base a las necesidades del publico")
    classJefeArea.set_estrategia_publicidad("Comparar competencia y solicitudes de los clientes")
    classJefeArea.set_reporte_estadistico("Reporte de actividades realizadas")
    classJefeArea.set_reporte_incidentes("Reporte de incidencias sucedidas en turno")

    # Mostrar información
    print("Empleado:")
    print(classEmpleado.mostrar_informacion())

    print("\nArea:")
    print(classArea.mostrar_informacion())

    print("\nDirector:")
    print(classDirector.mostrar_informacion())

    print("\nGerente:")
    print(classGerente.mostrar_informacion())

    print("\nJefeArea:")
    print(classJefeArea.mostrar_informacion())

if __name__ == "__main__":
    main()
