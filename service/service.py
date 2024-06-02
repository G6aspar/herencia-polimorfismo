from abc import ABC, abstractmethod

class ExcepcionAuto(Exception):
    """Excepción personalizada para errores en los autos."""
    pass

class AutoAbstracto(ABC):
    @abstractmethod
    def conducir(self):
        pass

class AutoDeportivo(AutoAbstracto):
    def conducir(self):
        print("El auto deportivo está conduciendo a alta velocidad")

class AutoFamiliar(AutoAbstracto):
    def conducir(self):
        raise ExcepcionAuto("El auto familiar tiene un problema en el motor")