import modules.getClients as cliente 

from tabulate import tabulate


print(tabulate(cliente.getAllClientPaisRegionCiudad("Australia", "Sur"), tablefmt="grid"))

#coincidir australia y la region (pero si es none tambien mostrarla)
#sacar filtros, usuarios sin informacion, usuarios que tengan la misma region
#