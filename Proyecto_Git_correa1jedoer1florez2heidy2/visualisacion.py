import os
import modulos.funcionalidad
def menuprincipal(op : int):
    title = """
    *******************************************
    *          ELIMINACION DE DATOS         *
    *******************************************
    """
    menuprincipal = '1.eliminar datos \n2.editar \n3. Salir'
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