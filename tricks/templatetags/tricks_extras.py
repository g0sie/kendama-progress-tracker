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


def progress_color(rank: int) -> str:
    """returns bg color for progress bar"""
    colors = {
        1: "progress-bar-striped bg-dark text-white",
        2: "progress-bar-striped bg-secondary text-white",
        3: "progress-bar-striped bg-secondary text-white",
        4: "progress-bar-striped bg-secondary text-white",
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
    html_str += f'<div class="progress-bar {progress_color(rank)}" role="progressbar" '
    html_str += f'aria-valuenow="{land_count}" style="width: {percentage}%" '
    html_str += f'aria-valuemin="0" aria-valuemax="{max_value[rank]}">'
    html_str += f'{land_count}</div>'
    html_str += '</div>'
    return format_html(html_str)


@register.simple_tag
def button(rank: int, land_count: int, id: int):
    """returns +1 land_count button or rank up button"""
    max_value = {
        1: 10,
        2: 25,
        3: 50,
        4: 100,
    }
    if land_count < max_value[rank]:
        html_button = f'<button type="submit" name="land_{id}" class="btn btn-primary">+1</a>'
    else:
        html_button = f'<button type="submit" name="rankup_{id}" class="btn btn-primary">rank up</a>'
    return format_html(html_button)
