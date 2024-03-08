import storage.empleados as em 

# cevuelve un listado con el nombre, apellidos y email
# de los empleados  segun el codigo del jefe

def getAllNombreApellidoEmailJefe(codigo):
    nombreApellidoEmail = []

    for val in em.empleados:
        if(val.get("codigo_jefe") == codigo):
          
          nombreApellidoEmail.append(
             {
              "nombre": val.get("nombre"),
            "apellido": f"({val.get('apellido1')} {val.get('apellido2')})",
            "email": val.get("email"),
            "jefe": val.get("codigo_jefe")
             }
            )
             
    return nombreApellidoEmail


# devuelve el nombre del puesto, nombre, apellido y email del jefe de la empresa 

def getAllNombrePuestoNombreApellidoEmail():
    NombrePuestoNombreApellidoEmail = []
    for val in em.empleados:
        if (val.get("codigo_jefe")) == None:
            NombrePuestoNombreApellidoEmail.append({
                "puesto": val.get("puesto"),
                "nombre": val.get("nombre"),
                "apellidos": f"{val.get('apellido1')} {val.get('apellido2')}",
                "email": val.get("email")
            })
    return NombrePuestoNombreApellidoEmail

# devuelve un listado con el nombre, apellidos y puesto de aquellos empleados
# que no sean representantes de ventas

def getNoRepresentanteDeVentas():
    NoRepresentanteDeVentas=[]
    for val in em.empleados:
        if(val.get("puesto") != "Representante Ventas"):
            NoRepresentanteDeVentas.append(
                {
                    "nombre": val.get("puesto"),
                    "apellidos": f"{val.get('apellido1')} {val.get('apellido2')}",
                    "puesto": val.get("puesto")
                }
            )
    return NoRepresentanteDeVentas

def menu():
    print(""" 

       __       __                                      ________                          __                            __                     
      |  \     /  \                                    |        \                        |  \                          |  \                    
      | $$\   /  $$  ______   _______   __    __       | $$$$$$$$ ______ ____    ______  | $$  ______    ______    ____| $$  ______    _______ 
      | $$$\ /  $$$ /      \ |       \ |  \  |  \      | $$__    |      \    \  /      \ | $$ /      \  |      \  /      $$ /      \  /       \
      | $$$$\  $$$$|  $$$$$$\| $$$$$$$\| $$  | $$      | $$  \   | $$$$$$\$$$$\|  $$$$$$\| $$|  $$$$$$\  \$$$$$$\|  $$$$$$$|  $$$$$$\|  $$$$$$$
      | $$\$$ $$ $$| $$    $$| $$  | $$| $$  | $$      | $$$$$   | $$ | $$ | $$| $$  | $$| $$| $$    $$ /      $$| $$  | $$| $$  | $$ \$$    \ 
      | $$ \$$$| $$| $$$$$$$$| $$  | $$| $$__/ $$      | $$_____ | $$ | $$ | $$| $$__/ $$| $$| $$$$$$$$|  $$$$$$$| $$__| $$| $$__/ $$ _\$$$$$$\
      | $$  \$ | $$ \$$     \| $$  | $$ \$$    $$      | $$     \| $$ | $$ | $$| $$    $$| $$ \$$     \ \$$    $$ \$$    $$ \$$    $$|       $$
       \$$      \$$  \$$$$$$$ \$$   \$$  \$$$$$$        \$$$$$$$$ \$$  \$$  \$$| $$$$$$$  \$$  \$$$$$$$  \$$$$$$$  \$$$$$$$  \$$$$$$  \$$$$$$$ 
                                                                               | $$                                                            
                                                                               | $$                                                            
                                                                                \$$                                                            
                                                                                                                   
          1. Ver los empleados de cada jefe (codigo jefe)
          2. 

""")