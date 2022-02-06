from django import template

register = template.Library()


@register.simple_tag
def card_color(rank: int) -> str:
    """returns css color for card"""
    colors = {
        1: "bg-secondary text-white",
        2: "bg-dark text-white",
        3: "bg-light text-dark",
        4: "bg-danger text-white",
        5: "bg-warning text-dark",
        6: "bg-info text-dark",
    }
    return colors[rank]


@register.simple_tag
def progress_color(rank: int) -> str:
    """returns css color for progress bar"""
    colors = {
        1: "progress-bar-striped bg-dark text-white",
        2: "progress-bar-striped bg-secondary text-white",
        3: "progress-bar-striped bg-secondary text-white",
        4: "progress-bar-striped bg-secondary text-white",
        5: "progress-bar-striped bg-secondary text-white",
        6: "progress-bar-striped text-white",
    }
    return colors[rank]
