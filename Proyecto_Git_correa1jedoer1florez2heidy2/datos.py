import modulos.editar as me
import modulos.funcionalidad as mf
def menuprincipal2(op : int):
    title = """
    *******************************************
    *          ELIMINACION DE DATOS         *
    *******************************************
    """
    menuprincipal = '1.eliminar datos \n2.editar \n3. Salir'
    if (op != 3):
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
                   mf.eliminar()
                case 2:
                    me.editar()
                case 3:
                    import main
                    main.menuprincipal
                case _:
                    menuprincipal2
