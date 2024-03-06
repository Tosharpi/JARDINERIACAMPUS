#import modules.getClients as cliente 
from tabulate import tabulate

import modules.getClients as cli



#print(tabulate(cliente.getNombreContacto(1)))
#coincidir australia y la region (pero si es none tambien mostrarla)
#sacar filtros, usuarios sin informacion, usuarios que tengan la misma region
#

#print(tabulate(cliente.getNombreContacto(1)))

#print(tabulate(ped.getCodigoPedido(1)))

print(tabulate(cli.getNombreContacto(1)))