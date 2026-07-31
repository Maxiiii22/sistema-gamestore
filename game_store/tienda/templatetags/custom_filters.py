from django import template

register = template.Library()

@register.filter
def punto_miles(value):
    """
    Formatea números con punto como separador de miles.
    Ej: 1000000 → '1.000.000'
    """
    try:
        return f"{int(value):,}".replace(",", ".")
    except (ValueError, TypeError):
        return value