from django import template
from datetime import datetime


register = template.Library()


@register.filter
def format_date(value):
    then = datetime.fromtimestamp(value)
    now = datetime.now()
    result = (now - then).total_seconds()

    mins = int(result // 60)
    hours = int(result // 3600)

    if mins < 10:
        date = 'только что'
    elif hours == 1 or hours == 21:
        date = f'{hours} час назад'
    elif 1 < hours < 5 or 21 < hours < 24:
        date = f'{hours} часа назад'
    elif 4 < hours < 21:
        date = f'{hours} часов назад'
    else:
        date = datetime.strftime(then, '%Y-%m-%d')

    return date


@register.filter()
def format_score(value, default):
    if value < -5:
        score = 'низкий'
    elif -5 <= value <= 5:
        score = 'средний'
    elif value > 5:
        score = 'высокий'
    else:
        score = default

    return score


@register.filter
def format_num_comments(value):
    if value == 0:
        comments_count = 'Оставьте комментарий'
    elif 0 < value <= 50:
        comments_count = value
    else:
        comments_count = '50+'

    return comments_count


@register.filter
def format_selftext(value, count):
    words = value.split(' ')
    beginning = words[0:count]
    ending = words[-count:]

    if value:
        short_info = f'{" ".join(beginning)} ... {" ".join(ending)}'
    else:
        short_info = value

    return short_info
