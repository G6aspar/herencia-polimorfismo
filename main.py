from service.service import AutoDeportivo, AutoFamiliar
from controller.controller import ControladorAuto

def main():
    auto_deportivo = AutoDeportivo()
    controlador_auto_deportivo = ControladorAuto(auto_deportivo)
    controlador_auto_deportivo.ejecutar_conduccion()

    auto_familiar = AutoFamiliar()
    controlador_auto_familiar = ControladorAuto(auto_familiar)
    controlador_auto_familiar.ejecutar_conduccion()

if __name__ == "__main__":
    main()