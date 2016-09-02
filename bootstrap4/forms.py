
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.admin.widgets import AdminFileWidget
from django.forms import (
    HiddenInput, FileInput, CheckboxSelectMultiple, Textarea, TextInput,
    PasswordInput
)
from django.forms.widgets import CheckboxInput
from django.utils.safestring import mark_safe

from bootstrap4.bootstrap import (
    get_bootstrap_setting, get_form_renderer, get_field_renderer,
    get_formset_renderer
)
from bootstrap4.text import text_concat, text_value
from bootstrap4.exceptions import BootstrapError
from bootstrap4.utils import add_css_class, render_tag, split_css_classes
from bootstrap4.components import render_icon


FORM_GROUP_CLASS = 'form-group row'


def render_formset(formset, **kwargs):
    renderer_cls = get_formset_renderer(**kwargs)
    return renderer_cls(formset, **kwargs).render()


def render_formset_errors(formset, **kwargs):
    renderer_cls = get_formset_renderer(**kwargs)
    return renderer_cls(formset, **kwargs).render_errors()


def render_form(form, **kwargs):
    renderer_cls = get_form_renderer(**kwargs)
    return renderer_cls(form, **kwargs).render()


def render_form_errors(form, type='all', **kwargs):
    renderer_cls = get_form_renderer(**kwargs)
    return renderer_cls(form, **kwargs).render_errors()


def render_field(field, **kwargs):
    renderer_cls = get_field_renderer(**kwargs)
    return renderer_cls(field, **kwargs).render()


def render_label(content, label_for=None, label_class=None, label_title=''):
    attrs = {}
    if label_for:
        attrs['for'] = label_for
    if label_class:
        attrs['class'] = label_class
    if label_title:
        attrs['title'] = label_title
    return render_tag('label', attrs=attrs, content=content)


def render_button(content, button_type=None, icon=None, button_class='', size='', href='', name=None, value=None, title=None):
    attrs = {}
    classes = add_css_class('btn', button_class)
    size = text_value(size).lower().strip()
    if size == 'xs':
        classes = add_css_class(classes, 'btn-xs')
    elif size == 'sm' or size == 'small':
        classes = add_css_class(classes, 'btn-sm')
    elif size == 'lg' or size == 'large':
        classes = add_css_class(classes, 'btn-lg')
    elif size == 'md' or size == 'medium':
        pass
    elif size:
        raise BootstrapError('Parameter "size" should be "xs", "sm", "lg" or empty ("{}" given).'.format(size))
    if button_type:
        if button_type == 'submit':
            classes = add_css_class(classes, 'btn-primary')
            attrs['class'] = 'btn btn-primary'
        elif button_type == 'reset':
            attrs['class'] = 'btn btn-warning'
        elif button_type not in ('reset', 'button', 'link'):
            raise BootstrapError('Parameter "button_type" should be "submit", "reset", "button", "link" or empty ("{}" given).'.format(button_type))
        attrs['type'] = button_type
        icon_content = render_icon(icon) if icon else ''
        if href:
            attrs['href'] = href
            tag = 'a'
        else:
            tag = 'button'
        if name:
            attrs['name'] = name
        if value:
            attrs['value'] = value
        if title:
            attrs['title'] = title
        return render_tag(tag, attrs=attrs, content=mark_safe(text_concat(icon_content, content, separator=' ')))


def render_field_and_label(field, label, field_class='', label_for=None, label_class='', layout='', **kwargs):
    if layout == 'horizontal':
        if not label_class:
            label_class = get_bootstrap_setting('horizontal_label_class')
        if not field_class:
            field_class = get_bootstrap_setting('horizontal_field_class')
        if not label:
            label = mark_safe('&#160;')
        label_class = add_css_class(label_class, 'col-form-label')
    html = field
    if field_class:
        html = '<div class="{klass}">{html}</div>'.format(klass=field_class, html=html)
    if label:
        html = render_label(label, label_for=label_for, label_class=label_class) + html
    return html


def render_form_group(content, css_class=FORM_GROUP_CLASS):
    return '<div class="{klass}">{content}</div>'.format(klass=css_class, content=content)


def is_widget_required_attribute(widget):
    if not get_bootstrap_setting('set_required'):
        return False
    if not widget.is_required:
        return False
    if isinstance(widget, (AdminFileWidget, HiddenInput, FileInput, CheckboxInput, CheckboxSelectMultiple)):
        return False
    return True


def is_widget_with_placeholder(widget):
    return isinstance(widget, (TextInput, Textarea, PasswordInput))
