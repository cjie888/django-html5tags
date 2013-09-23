# -*- coding:utf-8 -*-
import re

from django import forms
from django.forms.util import to_current_timezone
from django.forms.widgets import FILE_INPUT_CONTRADICTION
from django.conf import settings
from django.utils.datastructures import MultiValueDict, MergeDict
from django.utils.html import conditional_escape
from django.utils.translation import ugettext_lazy as _
from django.utils import formats
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe
from django.forms.util import flatatt
from django.utils.encoding import force_unicode


__all__ = (
    'TextInput', 'PasswordInput', 'HiddenInput', 'ClearableFileInput',
    'FileInput', 'DateInput', 'DateTimeInput', 'TimeInput', 'Textarea', 'MarkDownTextarea',
    'CheckboxInput', 'Select', 'NullBooleanSelect', 'SelectMultiple',
    'RadioSelect', 'CheckboxSelectMultiple', 'SearchInput', 'EmailInput', 'NumberInput',
    'IPAddressInput', 'MultiWidget', 'Widget', 'SplitDateTimeWidget',
    'SplitHiddenDateTimeWidget', 'MultipleHiddenInput',
)


class Widget(forms.Widget):
    is_required = False


class BootstrapInput(Widget):
    input_type = None # Subclasses must define this.

    def _format_value(self, value):
        if self.is_localized:
            return formats.localize_input(value)
        return value

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
        if value != '':
            # Only add the 'value' attribute if a value is non-empty.
            final_attrs['value'] = force_unicode(self._format_value(value))
        css_class = final_attrs.get('class', '')
        css_class += ' form-control'
        final_attrs['class'] = css_class
        return mark_safe(u'<input%s />' % flatatt(final_attrs))


class TextInput(BootstrapInput):
    input_type = 'text'


class PasswordInput(BootstrapInput, forms.PasswordInput):
    input_type = 'password'


class HiddenInput(BootstrapInput):
    input_type = 'hidden'
    is_hidden = True


class MultipleHiddenInput(HiddenInput, forms.MultipleHiddenInput):
    """<input type="hidden"> for fields that have a list of values"""
    pass


class IPAddressInput(TextInput):
    """<input type="text"> validating IP addresses with a pattern"""
    ip_pattern = ("(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25"
                  "[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}")


    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
        if value != '':
            # Only add the 'value' attribute if a value is non-empty.
            final_attrs['value'] = force_unicode(self._format_value(value))
        css_class = final_attrs.get('class', '')
        css_class += ' form-control'
        final_attrs['class'] = css_class
        final_attrs['pattern'] = self.ip_pattern
        return mark_safe(u'<input%s />' % flatatt(final_attrs))


class FileInput(forms.FileInput):
    pass


class ClearableFileInput(forms.ClearableFileInput):
    pass


class Textarea(Widget):
    rows = 10
    cols = 40

    def __init__(self, attrs=None):
        default_attrs = {'cols': self.cols, 'rows': self.rows}
        if attrs:
            default_attrs.update(attrs)
        super(Textarea, self).__init__(default_attrs)


    def render(self, name, value, attrs=None):
        if value is None: value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        css_class = final_attrs.get('class', '')
        css_class += ' form-control'
        final_attrs['class'] = css_class
        return mark_safe(u'<textarea%s>%s</textarea>' % (flatatt(final_attrs),
                conditional_escape(force_unicode(value))))


class MarkDownTextarea(Textarea):#(AdminTextareaWidget):
    rows = 10
    cols = 40

    class Media:
        js = (
            settings.STATIC_URL + 'markdown/markdown.js',
            settings.STATIC_URL + 'markdown/markDownEditor.js',
        )

        css = {
            'stylesheet': (
                settings.STATIC_URL + 'markdown/markDownEditor.css',
            )
        }


    def __init__(self, attrs=None):
        default_attrs = {'cols': self.cols, 'rows': self.rows}
        if attrs:
            default_attrs.update(attrs)
        super(MarkDownTextarea, self).__init__(default_attrs)


    def render(self, name, value, attrs=None):
        if value is None: value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        final_attrs['class'] = ' form-control'
        return mark_safe(u'<textarea%s>%s</textarea>' % (flatatt(final_attrs), conditional_escape(force_unicode(value)))+
                         """
                         <script type="text/javascript">$(function(){$("#"""+final_attrs['id']+"""").markDownEditor();})</script>
                         """)


class DateInput(BootstrapInput, forms.DateInput):
    def render(self, name, value, attrs=None):
        date_input_attrs = {}
        if attrs:
            date_input_attrs.update(attrs)
        date_format = self.format
        if not date_format:
            date_format = 'yyyy-mm-dd'
        date_input_attrs.update({
            'data-date-format': 'yyyy-mm-dd',
            'data-date-language': 'en',
            'data-bootstrap-widget': 'datepicker',
            'class': 'form-control'
        })
        attrs['class'] = 'form-control'
        return mark_safe(super(DateInput, self).render(name, value, attrs=date_input_attrs)+
                         """<script>$("#"""+attrs['id']+"""").datetimepicker({
                         keyboardNavigation: true,
                         todayBtn: true,
                         todayHighlight: true,
                         startView: 1}, "update");
                         </script>
                         """)


class DateTimeInput(forms.DateInput):
    def render(self, name, value, attrs=None):
        date_input_attrs = {}
        if attrs:
            date_input_attrs.update(attrs)
        date_format = self.format
        if not date_format:
            date_format = 'yyyy-mm-dd hh:ii:ss'
        date_input_attrs.update({
            'data-date-format': 'yyyy-mm-dd hh:ii:ss',
            'data-date-language': 'en',
            'data-bootstrap-widget': 'datepicker',
            'class': 'form-control'
        })
        attrs['class'] = 'form-control'
        return mark_safe(super(DateTimeInput, self).render(name, value, attrs=date_input_attrs)+
                         """<script>$("#"""+attrs['id']+"""").datetimepicker({
                         keyboardNavigation: true,
                         todayBtn: true,
                         todayHighlight: true,
                         startView: 1}, "update");
                         </script>
                         """)


class TimeInput(forms.DateInput):
    def render(self, name, value, attrs=None):
        date_input_attrs = {}
        if attrs:
            date_input_attrs.update(attrs)
        date_format = self.format
        if not date_format:
            date_format = 'hh:ii:ss'
        date_input_attrs.update({
            'data-date-format': 'hh:ii:ss',
            'data-date-language': 'en',
            'data-bootstrap-widget': 'datepicker',
            'class': 'form-control'
        })
        attrs['class'] = 'form-control'
        return mark_safe(super(TimeInput, self).render(name, value, attrs=date_input_attrs)+
                         """<script>$("#"""+attrs['id']+"""").datetimepicker({
                         keyboardNavigation: true,
                         todayBtn: true,
                         todayHighlight: true,
                         startView: 1}, "update");
                         </script>""")


class SearchInput(BootstrapInput):
    input_type = 'search'


class EmailInput(BootstrapInput):
    input_type = 'email'


class NumberInput(BootstrapInput):
    input_type = 'number'
    min = None
    max = None
    step = None

    def __init__(self, attrs=None):
        default_attrs = {'min': self.min, 'max': self.max, 'step': self.step}
        if attrs:
            default_attrs.update(attrs)
        # Popping attrs if they're not set
        for key in list(default_attrs.keys()):
            if default_attrs[key] is None:
                default_attrs.pop(key)
        super(NumberInput, self).__init__(default_attrs)


def boolean_check(v):
    return not (v is False or v is None or v == '')


class CheckboxInput(forms.CheckboxInput):
    input_type = 'checkbox'


class Select(forms.Select):
    allow_multiple_selected = False

    def __init__(self, attrs=None, choices=()):
        super(Select, self).__init__(attrs)
        self.choices = list(choices)

    def render(self, name, value, attrs=None, choices=()):
        if value is None: value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        final_attrs['class'] = 'form-control'
        output = [u'<select%s>' % flatatt(final_attrs)]
        options = self.render_options(choices, [value])
        if options:
            output.append(options)
        output.append(u'</select>')
        return mark_safe(u'\n'.join(output))


class NullBooleanSelect(Select, forms.NullBooleanSelect):

    """
    A Select Widget intended to be used with NullBooleanField.
    """
    def __init__(self, attrs=None):
        choices = ((u'1', _('Unknown')),
                   (u'2', _('Yes')),
                   (u'3', _('No')))
        super(NullBooleanSelect, self).__init__(attrs, choices)

    def render(self, name, value, attrs=None, choices=()):
        try:
            value = {True: u'2', False: u'3', u'2': u'2', u'3': u'3'}[value]
        except KeyError:
            value = u'1'
        return super(NullBooleanSelect, self).render(name, value, attrs, choices)

    def value_from_datadict(self, data, files, name):
        value = data.get(name, None)
        return {u'2': True,
                True: True,
                'True': True,
                u'3': False,
                'False': False,
                False: False}.get(value, None)

    def _has_changed(self, initial, data):
        # For a NullBooleanSelect, None (unknown) and False (No)
        # are not the same
        if initial is not None:
            initial = bool(initial)
        if data is not None:
            data = bool(data)
        return initial != data


class SelectMultiple(Select, forms.SelectMultiple):
    allow_multiple_selected = True

    def render(self, name, value, attrs=None, choices=()):
        if value is None: value = []
        final_attrs = self.build_attrs(attrs, name=name)
        output = [u'<select class="form-control"  multiple="multiple"%s>' % flatatt(final_attrs)]
        options = self.render_options(choices, value)
        if options:
            output.append(options)
        output.append('</select>')
        return mark_safe(u'\n'.join(output))


class RadioSelect(forms.RadioSelect):#Select):
    pass


class CheckboxSelectMultiple(SelectMultiple):
    pass


class MultiWidget(forms.MultiWidget):
    pass


class SplitDateTimeWidget(MultiWidget):
    def __init__(self, attrs=None, date_format=None, time_format=None):
        widgets = (DateInput(attrs=attrs, format=date_format),
                   TimeInput(attrs=attrs, format=time_format))
        super(SplitDateTimeWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            value = to_current_timezone(value)
            return [value.date(), value.time().replace(microsecond=0)]
        return [None, None]


class SplitHiddenDateTimeWidget(SplitDateTimeWidget):
    is_hidden = True

    def __init__(self, attrs=None, date_format=None, time_format=None):
        super(SplitHiddenDateTimeWidget, self).__init__(attrs, date_format,
                                                        time_format)
        for widget in self.widgets:
            widget.input_type = 'hidden'
            widget.is_hidden = True
