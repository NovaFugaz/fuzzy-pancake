from django import template

register = template.Library()

@register.filter
def add_class(field, css_classes):
    return field.as_widget(attrs={'class': css_classes})
