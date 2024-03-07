#import modules.getClients as cliente 
from tabulate import tabulate

import modules.getClients as cliente
import modules.getOficina as oficina
import modules.getEmpleado as empleado
import modules.getPedido as pedido
import modules.getPago as pago

#print(tabulate(cliente.getNombreContacto(1)))
#coincidir australia y la region (pero si es none tambien mostrarla)
#sacar filtros, usuarios sin informacion, usuarios que tengan la misma region
#

#print(tabulate(cliente.getNombreContacto(1)))

#print(tabulate(ped.getCodigoPedido(1)))

#print(tabulate(cli.getNombreContacto(1)))

#print(oficina.getAllCiudadTelefono("España"))

#print(tabulate(empleado.em.empleados))

#print(tabulate(empleado.getAllNombrePuestoNombreApellidoEmail(), tablefmt="grid"))

print(tabulate(pago.getAllFormasPago(), tablefmt="grid"))