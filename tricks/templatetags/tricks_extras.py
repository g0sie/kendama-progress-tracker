from django import template

register = template.Library()


@register.simple_tag
def color(rank: int) -> str:
    """returns css color"""
    colors = {
        1: "bg-secondary text-white",
        2: "bg-dark text-white",
        3: "bg-light text-dark",
        4: "bg-danger text-white",
        5: "bg-warning text-dark",
        6: "bg-info text-dark",
    }
    return colors[rank]
