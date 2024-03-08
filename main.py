#import modules.getClients as cliente 
from tabulate import tabulate
import sys
import modules.getClients as cliente
import modules.getOficina as oficina
import modules.getEmpleado as empleado
import modules.getPedido as pedido
import modules.getPago as pago

if __name__ == "__main__":
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
                    $. Pedido
    """)

    
opcion = int(input("Seleccione una de las opciones: "))  

if(opcion == 1):
    cliente.menu()
elif(opcion == 2):
    oficina.menu()
elif(opcion == 3):
    empleado.menu()

