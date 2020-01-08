
from . import procesos

def verificar(request):
    response = False
    if request.method == 'GET':
        if request.GET.get('layout') == 'Descargar Layout':
            response = True
    return response

def descargar(modelo):
    # Metodo GET para descargar layout del Modelo
    try:
        return procesos.obtenerLayout(modelo)
    except Exception as e:
        return None

def cargar(request,modelo):
    # Metodo para leer archivo de excel y cargar en Modelo
    try:
        file = request.FILES['excel']
        return procesos.leerExcel(file,modelo)
    except Exception as e:
        respuesta = {
            'resp' : 0, 
            'mensaje' : "Error: cargar()",
        }
        return respuesta