from atexit import register
from django import template

register = template.Library()

@register.filter(name="greeting")
def greeting(value):
    
    large = ''
    if len(value) >= 8:
        large = 'El valor ingresado es muy largo'
    
    return f"<h1 style='background:green; color:white'> Hola {value} </h1> " + large