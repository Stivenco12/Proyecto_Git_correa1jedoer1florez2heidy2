import os
import modulos.funcionalidad
def menuprincipal(op : int):
    title = """
    *******************************************
    *  GESTIONAMIENTOS DE LAS OPERACIONES 
                 EN  SUCURSALES               *
    *******************************************
    """
    menuprincipal = '1.ingresar sucursal \n2.editar datos de la sucursal\n3.visualisar sucursales \n4. Salir'
    if (op != 4):
        print(title)
        print(menuprincipal)
        try:
            op = int(input(":) "))
        except ValueError:
            print("Opcion no tiene formato adecuado")
            menuprincipal(0)
        else:
            match (op):
                case 1:
                   function.añadido(0)
                case 2:
                    (0)
                case 3:
                    (0)
                case _:
                    print()

menuprincipal(1)
     