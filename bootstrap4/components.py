# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms.widgets import flatatt
from django.utils.safestring import mark_safe
from bootstrap4.utils import render_tag
from bootstrap4.text import text_value


def render_icon(icon, tag='span', title=''):
    """
    Render a Bootstrap glyphicon icon
    """
    attrs = {
        'class': 'fa fa-{icon}'.format(icon=icon),
    }
    if title:
        attrs['title'] = title

    if tag:
        return render_tag(tag, attrs=attrs)
    else:
        return render_tag('span', attrs=attrs)


def render_alert(content, alert_type=None, dismissable=True):
    """
    Render a Bootstrap alert
    """
    button = ''
    if not alert_type:
        alert_type = 'info'
    css_classes = ['alert', 'alert-' + text_value(alert_type)]
    if dismissable:
        css_classes.append('alert-dismissable fade in')
        button = """
                <button type="button"
                        class="close"
                        data-dismiss="alert"
                        aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                </button>
                 """
    button_placeholder = '__BUTTON__'
    return mark_safe(render_tag(
        'div',
        attrs={'class': ' '.join(css_classes), 'role': 'alert'},
        content=button_placeholder + text_value(content),
    ).replace(button_placeholder, button))
