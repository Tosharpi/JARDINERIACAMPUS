#import modules.getClients as cliente 
from tabulate import tabulate
import modules.getClients as cliente
import modules.getOficina as oficina
import modules.getEmpleado as empleado
import modules.getPedido as pedido
import modules.getPago as pago
import modules.getProducto as prod

if __name__ == "__main__":

    while True:

        print(f"""

        __       __                                      _______             __                      __                      __ 
        |  \     /  \                                    |       \           |  \                    |  \                    |  $
        | $$\   /  $$  ______   _______   __    __       | $$$$$$$\  ______   \$$ _______    _______  \$$  ______    ______  | $$
        | $$$\ /  $$$ /      \ |       \ |  \  |  \      | $$__/ $$ /      \ |  \|       \  /       \|  \ /      \  |      \ | $$
        | $$$$\  $$$$|  $$$$$$\| $$$$$$$\| $$  | $$      | $$    $$|  $$$$$$\| $$| $$$$$$$\|  $$$$$$$| $$|  $$$$$$\  \$$$$$$\| $$
        | $$\$$ $$ $$| $$    $$| $$  | $$| $$  | $$      | $$$$$$$ | $$   \$$| $$| $$  | $$| $$      | $$| $$  | $$ /      $$| $$
        | $$ \$$$| $$| $$$$$$$$| $$  | $$| $$__/ $$      | $$      | $$      | $$| $$  | $$| $$_____ | $$| $$__/ $$|  $$$$$$$| $$
        | $$  \$ | $$ \$$     \| $$  | $$ \$$    $$      | $$      | $$      | $$| $$  | $$ \$$     \| $$| $$    $$ \$$    $$| $$
        \$$      \$$  \$$$$$$$ \$$   \$$  \$$$$$$        \$$       \$$       \$$ \$$   \$$  \$$$$$$$ \$$| $$$$$$$   \$$$$$$$ \$$
                                                                                                        | $$                    
                                                                                                        | $$                    
                                                                                                            \$$                    
                    1. Cliente
                    2. Oficina
                    3. Empleado
                    4. Pedido
                    5. Pago
                    6. Poductos
                    0. Salir
    """)

    
        opcion = int(input("Seleccione una de las opciones: "))  

        if(opcion == 1):
            cliente.menu()
        elif(opcion == 2):
            oficina.menu()
        elif(opcion == 3):
            empleado.menu()
        elif(opcion == 4):
            pedido.menu()
        elif(opcion == 5):
            pago.menu()
        elif(opcion == 6):
            prod.menu()
        elif(opcion == 0):
            break

