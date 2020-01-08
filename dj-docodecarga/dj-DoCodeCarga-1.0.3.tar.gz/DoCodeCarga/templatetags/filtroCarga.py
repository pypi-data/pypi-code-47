from django import template
register = template.Library()

# Colocar filtros de la aplicacion aqui
@register.filter(name='filtroPrueba')
def filtroPrueba(registro):
    registros = list()
    return registros

