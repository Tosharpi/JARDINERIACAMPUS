#import modules.getClients as cliente 
from tabulate import tabulate
import sys
import modules.getClients as cliente
import modules.getOficina as oficina
import modules.getEmpleado as empleado
import modules.getPedido as pedido
import modules.getPago as pago


#print(tabulate(pago.getAllFormasPago(), tablefmt="grid"))

#def menu():
#    contador = 1
#    print("menu principal")

#    for nombre, objeto in sys.modules.items():
#        if nombre.startswith("modules"):
#            modulo = getattr(objeto, "__name__", None)
#            if(modulo != "modules"):
#                print(f""" {contador} {modulo.split("get")[-1]}""")
#   
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
    cliente.menuCli()
elif(opcion == 2):
    oficina.menu()
elif(opcion == 3):
    empleado.menu()

