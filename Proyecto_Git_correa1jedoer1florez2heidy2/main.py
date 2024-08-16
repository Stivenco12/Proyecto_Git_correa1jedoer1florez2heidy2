import os
import modulos.funcionalidad as mf
import visualisar as vi
import datos as da
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
                    mf.añadido
                case 2:
                    da.menuprincipal
                case 3:
                    vi.menuprincipal
                case _:
                    print()

menuprincipal(1)
     