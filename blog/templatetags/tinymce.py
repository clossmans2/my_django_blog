from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag(takes_context=True)
def add_tinymce(context):
    init_script = """
    <script type="text/javascript">
        var config = {
            selector: 'textarea',
            plugins : 'advlist anchor autolink autoresize code colorpicker emoticons fullscreen hr image imagetools insertdatetime link lists media nonbreaking pagebreak paste searchreplace spellchecker tabfocus table textcolor visualblocks visualchars wordcount',
            themes: 'modern',
            menubar: 'tools edit insert view format table',
            toolbar1: 'undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image',
            toolbar2: 'media | forecolor backcolor emoticons',
            image_advtab: true,
        };
        tinymce.init(config);
        $(document).on('focusin', function(e) {
          if ($(e.target).closest(".mce-window").length) {
            e.stopImmediatePropagation();
          }
        });
        </script>
    """
    if context['prod']:
        script = "<script src='https://cdn.tinymce.com/4/tinymce.min.js'></script>"
    else:
        script = """<script src="/static/js/tinymce.min.js" type="text/javascript"></script>"""

    output = "%s \n %s" % (script, init_script)
    return mark_safe(output)


@register.simple_tag(takes_context=True)
def add_tinymce_to_selector(context, selector='textarea'):
    init_script = """
    <script type="text/javascript">
        var config = {
            selector: '%s',
            plugins : 'advlist anchor autolink autoresize code colorpicker emoticons fullscreen hr image imagetools insertdatetime link lists media nonbreaking pagebreak paste searchreplace spellchecker tabfocus table textcolor visualblocks visualchars wordcount',
            themes: 'modern',
            menubar: 'tools edit insert view format table',
            toolbar1: 'undo redo | styleselect | bold italic | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | link image',
            toolbar2: 'media | forecolor backcolor emoticons',
            image_advtab: true,
        };
        tinymce.init(config);
        $(document).on('focusin', function(e) {
          if ($(e.target).closest(".mce-window").length) {
            e.stopImmediatePropagation();
          }
        });
        </script>
    """ % selector
    if context['prod']:
        script = "<script src='https://cdn.tinymce.com/4/tinymce.min.js'></script>"
    else:
        script = """<script src="/static/js/tinymce.min.js" type="text/javascript"></script>"""
    output = "%s \n %s" % (script, init_script)
    return mark_safe(output)
