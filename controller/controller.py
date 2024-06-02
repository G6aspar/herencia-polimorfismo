from service.service import AutoAbstracto, ExcepcionAuto

class ControladorAuto:
    def __init__(self, auto: AutoAbstracto):
        self.auto = auto

    def ejecutar_conduccion(self):
        try:
            self.auto.conducir()
        except ExcepcionAuto as e:
            print(f"Excepción capturada en ControladorAuto: {e}")