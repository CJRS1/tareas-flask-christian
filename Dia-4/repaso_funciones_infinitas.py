def prueba(**argumentos):
    print(argumentos)

prueba(nombre='eduacr',apellido='dasda')

persona ={
    'nombre':'edu',
    'apellido':'dasd'
}

prueba(persona=persona)

prueba(**persona)
prueba(nombre=persona['nombre'],apellido=persona['apellido'])

def saludar(nombre):
    print(nombre)

usuario ={
    'nombre':'eduardo'
}

usuario2 ={
    'nombrecito':'juanito'
}

saludar(**usuario)

saludar(**usuario2)