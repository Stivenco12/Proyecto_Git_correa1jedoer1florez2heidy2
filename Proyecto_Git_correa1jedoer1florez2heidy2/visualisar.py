
def menuprincipal1(op : int):
    title = """
    *******************************************
    *       VISUALISACIONES SUCURSALES       *
    *******************************************
    """
    menuprincipal = '1.ver sucursales \n2.filtrado por nombre\n3.filtrado por estado \n4. Salir'
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
