from django import template
from django.utils.html import format_html

register = template.Library()


@register.simple_tag
def card_color(rank: int) -> str:
    """returns bg color for card"""
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
def button_color(rank: int) -> str:
    """returns color for button"""
    colors = {
        1: "btn-secondary",
        2: "btn-dark",
        3: "btn-light",
        4: "btn-danger",
        5: "btn-warning text-dark",
        6: "btn-info text-dark",
    }
    return colors[rank]


@register.simple_tag
def list_color(rank: int) -> str:
    """returns color for card body"""
    colors = {
        1: "list-group-item-secondary",
        2: "list-group-item-dark",
        3: "list-group-item-light",
        4: "list-group-item-danger",
        5: "list-group-item-warning",
        6: "list-group-item-info",
    }
    return colors[rank]


@register.simple_tag
def progress_bar(rank: int, land_count: int):
    """returns html progress bar"""
    max_value = {
        1: 10,
        2: 25,
        3: 50,
        4: 100,
    }
    land_count = min(land_count, max_value[rank])
    percentage = land_count / max_value[rank] * 100
    html_str = '<div class="progress">'
    html_str += f'<div class="progress-bar {card_color(rank)}" role="progressbar" '
    html_str += f'aria-valuenow="{land_count}" style="width: {percentage}%" '
    html_str += f'aria-valuemin="0" aria-valuemax="{max_value[rank]}">'
    html_str += f'{land_count}/{max_value[rank]}</div>'
    html_str += '</div>'
    return format_html(html_str)


@register.simple_tag
def get_is_rank_up(rank: int, land_count: int):
    """returns true if the trick meet the requirements to rank up"""
    max_value = {
        1: 10,
        2: 25,
        3: 50,
        4: 100,
    }
    if land_count >= max_value[rank]:
        return True
    return False
